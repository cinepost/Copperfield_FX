/*%g++ -o deepmplay %
 *
 * Produced by:
 *	Side Effects Software Inc
 *	477 Richmond Street West
 *	Toronto, Ontario
 *	Canada   M5V 3E7
 *	416-504-9876
 *
 * NAME:	deepmplay.C
 *
 * COMMENTS:
 *	This application is an example of writing deep raster images to the
 *	imdisplay application.  It is intended to be used as instructional code
 *	to write display drivers for renderers etc.
 *
 *	As written, the program will write three planes of constant color image
 *	to mplay.
 */

#include <sys/types.h>
#include <netinet/in.h>
#include <malloc.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>

//
// The magic number is the first integer of the header passed on the pipe
//

#define MAGIC	(('h'<<24)+('M'<<16)+('P'<<8)+('0'))

#define XRES	320		// Image X resolution
#define YRES	240		// Image Y resolution
#define TXRES	16		// Tile X resolution
#define TYRES	16		// Tile Y resolution
#define NX	(XRES/TXRES)	// Number of X tiles
#define NY	(YRES/TYRES)	// Number of Y tiles
#define NPLANES	3

struct PlaneDef {
    void	*myData;
    const char	*myName;

    //  DataFormat may be one of:
    //	0	= Floating point data
    //	1	= Unsigned char data
    //	2	= Unsigned short data
    //	4	= Unsigned int data
    int		 myFormat;

    //  ArraySize may be one of:
    //	1	= A single channel image
    //	3	= RGB data
    //	4	= RGBA data
    //  The pixel planes are packed so that the data
    //  is layed out as RGBRGBRGB... not RRRGGGBBB...
    int		 myArraySize;

    int		 myPixelSize;
};

PlaneDef thePlanes[NPLANES] = {
    { 0, "C",		1,	4, 0 },	// C plane is unsigned char, RGBA
    { 0, "s",		0,	1, 0 },	// s plane is float, single channel
    { 0, "Normal",	0,	3, 0 }	// N plane is float, RGB data
};

// Define how many bytes are required for each channel
#define DATABYTES(format)	(format == 0 ? sizeof(float) : format)

static void
freeTileData()
{
    int		i;
    for (i = 0; i < NPLANES; i++)
	::free(thePlanes[i].myData);
}

static void
buildTiles()
{
    int			 pixels, words, bytes;
    int			 i, c;
    unsigned short	*sdata;
    unsigned char	*cdata;
    unsigned int	*idata;
    float		*fdata;

    // Allocate storage for the tile
    for (i = 0; i < NPLANES; i++)
    {
	pixels  = TXRES * TYRES;
	words = pixels * thePlanes[i].myArraySize;
	bytes = words * DATABYTES(thePlanes[i].myFormat);
	thePlanes[i].myData = ::malloc(bytes);

	// Compute how many bytes per pixel there are
	thePlanes[i].myPixelSize = thePlanes[i].myArraySize *
				   DATABYTES(thePlanes[i].myFormat);

	cdata = (unsigned char *)thePlanes[i].myData;
	sdata = (unsigned short *)thePlanes[i].myData; 
	idata = (unsigned int *)thePlanes[i].myData; 
	fdata = (float *)thePlanes[i].myData;

	// Just fill in with some constant values.
	for (c = 0; c < words; c++)
	{
	    switch (thePlanes[i].myFormat)
	    {
		case 1:		*cdata++ = 0x85; break;
		case 2:		*sdata++ = 0x8512; break;
		case 4:		*idata++ = 0x84123456; break;
		default:	*fdata++ = 0.763;
	    }
	}
    }
}

static void
sendPlaneDefinitions(FILE *fp)
{
    int		plane_def[8];
    int		name_length;
    int		i;
    // Transmit the plane definitions
    ::memset(plane_def, 0, sizeof(plane_def));
    for (i = 0; i < NPLANES; i++)
    {
	name_length = ::strlen(thePlanes[i].myName);

	plane_def[0] = i;				// Plane index
	plane_def[1] = name_length;	// Length of the plane
	plane_def[2] = thePlanes[i].myFormat;
	plane_def[3] = thePlanes[i].myArraySize;
	if (fwrite(plane_def, sizeof(int), 8, fp) != 8)
	{
	    ::fprintf(stderr, "Error sending plane definition: %d\n", i);
	    ::exit(1);
	}
	if (fwrite(thePlanes[i].myName, sizeof(char),
			    name_length, fp) != name_length)
	{
	    ::fprintf(stderr, "Error sending plane name: %d\n", i);
	    ::exit(1);
	}
    }
}

static void
writeTile(FILE *fp, int tx0, int tx1, int ty0, int ty1)
{
    int		tile_head[4];
    int		i;
    size_t	size;

    for (i = 0; i < NPLANES; i++)
    {
	if (NPLANES > 1)
	{
	    // First, tell the reader what the plane index is for the data
	    // being sent.  This is done by sending a special tile header.
	    // The x0 coordinate is set to -1 to indicate the special
	    // header.  The x1 coordinate is set to the plane index.  The Y
	    // coordinates must be zero.
	    tile_head[0] = -1;
	    tile_head[1] =  i;
	    tile_head[2] =  0;
	    tile_head[3] =  0;
	    if (fwrite(tile_head, sizeof(int), 4, fp) != 4)
	    {
		::fprintf(stderr, "Error writing plane for tile: %d %d %d %d\n",
				tx0, tx1, ty0, ty1);
		::exit(1);
	    }
	}

	// Fill out the tile header
	tile_head[0] = tx0;
	tile_head[1] = tx1;
	tile_head[2] = ty0;
	tile_head[3] = ty1;
	size = (tx1 - tx0 + 1) * (ty1 - ty0 + 1);

	// Write the tile header to the pipe
	if (fwrite(tile_head, sizeof(int), 4, fp) != 4)
	{
	    ::fprintf(stderr, "Error writing tile: %d %d %d %d\n",
			    tx0, tx1, ty0, ty1);
	    ::exit(1);
	}
	// Write the data to the pipe
	if (fwrite(thePlanes[i].myData, thePlanes[i].myPixelSize,
				size, fp) != size)
	{
	    ::fprintf(stderr, "Error writing data: %d %d %d %d\n",
			    tx0, tx1, ty0, ty1);
	    ::exit(1);
	}
    }
}

static inline int SYSmin(int a, int b) { return a < b ? a : b; }

int
main(int argc, char *argv[])
{
    char	 cmd[512];
    int		 header[8];
    int		 tx, ty;
    FILE	*fp;

    // To send images to the IPR, you'd need to specify the port number
    // using the -s option. This can be retrieved in soho by evaluating the
    // vm_image_mplay_socketport property.

    ::strcpy(cmd, "imdisplay -p");
    ::strcat(cmd, " -n deepmplay");	// Set the name of the image
    //
    // If the first scanline of the image is at the top, the -f option should
    // be specified.
    //::strcat(cmd, " -f");			// Flip the image

    fp = ::popen(cmd, "w");
    if (!fp)
    {
	::fprintf(stderr, "Unable to open imdisplay\n");
	::exit(1);
    }

    ::memset(header, 0, sizeof(header));
    header[0] = MAGIC;
    header[1] = XRES;
    header[2] = YRES;

    // When NPLANES is 1, the protocol to transmit an image to imdisplay
    // can be simpler (although the deep raster approach will still work
    // even with 1 plane).  Here, the format for the only plane can be
    // specified in the main header rather than in a subsequent write.
    if (NPLANES == 1)
    {
	header[3] = thePlanes[0].myFormat;
	header[4] = thePlanes[0].myArraySize;
    }
    else
	header[5] = NPLANES;

    if (fwrite(header, sizeof(int), 8, fp) != 8)
    {
	::fprintf(stderr, "Unable to write header\n");
	::exit(1);
    }

    if (NPLANES > 1)
	::sendPlaneDefinitions(fp);

    ::buildTiles();		// Build the tile to write
    for (ty = 0; ty < YRES; ty += TYRES)
	for (tx = 0; tx < XRES; tx += TXRES)
	    ::writeTile(fp,
		    tx, SYSmin(tx+TXRES, XRES)-1,
		    ty, SYSmin(ty+TYRES, YRES)-1);

    ::pclose(fp);
    ::freeTileData();
}
