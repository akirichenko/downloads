# downloads


========================================================
  - New script: localrepo/tools/validate_key_checks.sh
  - Runbook updated: localrepo/LOCALREPO_MAINTENANCE.md

  What the script checks each run:

  - python3.11-psutil regression guard:
      - Fails if RPM requires GLIBC_ABI_DT_RELR
      - Runs dnf ... install glances --assumeno and requires Transaction Summary
  - perf / kernel-headers conflict guard:
      - Fails if perf RPM contains /usr/include/perf/perf_dlfilter.h
      - If kernel-headers exists, runs dnf ... install perf kernel-headers --assumeno
      - If not, runs dnf ... install perf --assumeno

  I ran it once now:

  - 5 passed, 0 failed

  Use:

  /dump/tmp/localrepo/tools/validate_key_checks.sh

