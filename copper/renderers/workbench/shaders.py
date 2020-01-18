class SURFACE():
    VS = '''
    #version 330

    uniform mat4 model;
    uniform mat4 view;
    uniform mat4 projection;

    in vec3 in_vert;
    in vec3 in_norm;
    
    out vec3 v_vert;
    out vec3 v_norm;
    out vec3 v_color;

    void main() {
        v_vert = in_vert;
        v_norm = in_norm;
        v_color = vec3(1.0, 1.0, 1.0);
        gl_Position = projection * view * model * vec4(in_vert, 1.0);
    }
    '''

    FS = '''
    #version 330

    in vec3 v_vert;
    in vec3 v_norm;
    in vec3 v_color;

    out vec4 f_color;

    void main() {
        vec3 Light = vec3(5.0, 5.0, 5.0);

        float lum = dot(normalize(v_norm), normalize(v_vert - Light));
        lum = acos(lum) / 3.14159265;
        lum = clamp(lum, 0.0, 1.0);
        lum = lum * lum;
        lum = smoothstep(0.0, 1.0, lum);
        lum *= smoothstep(0.0, 80.0, v_vert.z) * 0.3 + 0.7;
        lum = lum * 0.8 + 0.2;
        f_color = vec4(v_color * lum, 1.0);
    }
'''