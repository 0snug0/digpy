# digpy

## Create a config file

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