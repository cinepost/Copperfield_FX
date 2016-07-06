class RegistryMeta(type):
    def __getitem__(meta, key):
        return meta._registry[key]