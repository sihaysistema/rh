## RH

Recursos Humanos - Si Hay Sistema

Reference: https://ipip.ori.org/newAB5CKey.htm

---

### How to Install

> Tip: before installing it is recommended to create a snapshot to the server.

1. `bench get-app --branch production https://github.com/sihaysistema/rh.git`
2. `bench setup requirements`
3. `bench build --app rh`
4. `bench restart`
5. `bench --site [your.site.name] install-app rh`
6. `bench --site [your.site.name] migrate`

---

### How to uninstall

> Tip: before uninstalling create a snapshot of your server.

> Note: Some custom fields with data may not be completely removed, however this will not affect the performance of the system.

1. `bench --site site1.local uninstall-app rh`
2. `bench --site site1.local remove-app rh`

---
### How To Use:

[Wiki RH](https://github.com/sihaysistema/rh/wiki)

---

#### License

MIT