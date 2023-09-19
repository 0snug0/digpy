# digpy

## Create a config file

```
mkdir ~/.digpy
touch ~/.digpy/config.yml
```

Add the following config to your yaml
```
current-environment: main
current-product: secure
environments:
  - name: main
    url: https://secure.sysdig.com
    secure:
      token: xx
    monitor:
      token: xx
  - name: kubedemo
    url: https://secure.sysdig.com
    secure:
      token: xx
    monitor:
      token: xx
```

## Toolbox of examples
```
python3 digpy/toolbox/AKS-CVE-2023-29332.py
```

## Adding new endpoints
```
digapi.py - use this file to add new functional endpoints
digpy.py - this file has the functions for each method
```

### Todo
Adding more data models to models/ folder