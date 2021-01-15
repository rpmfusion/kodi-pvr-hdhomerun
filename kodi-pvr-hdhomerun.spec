%global kodi_addon pvr.hdhomerun
%global kodi_version 18.0
%global kodi_codename Leia

Name:           kodi-%(tr "." "-" <<<%{kodi_addon})
Version:        3.4.3
Release:        1%{?dist}
Summary:        HDHomeRun PVR for Kodi

License:        GPLv2+
URL:            https://github.com/kodi-pvr/%{kodi_addon}/
Source0:        %{url}/archive/%{version}-%{kodi_codename}/%{kodi_addon}-%{version}-%{kodi_codename}.tar.gz
Source1:        https://raw.githubusercontent.com/kodi-pvr/pvr.hdhomerun/4f2763c083a2fc099552794ae59aaf55516ead95/LICENSE.md

Patch0:         kodi-pvr-hdhomerun-cmake.patch

BuildRequires:  cmake3
BuildRequires:  gcc-c++
BuildRequires:  kodi-devel >= %{kodi_version}
BuildRequires:  kodi-platform-devel
BuildRequires:  platform-devel
BuildRequires:  jsoncpp-devel
BuildRequires:  hdhomerun-devel
Requires:       kodi >= %{kodi_version}
ExcludeArch:    %{power64} ppc64le

%description
%{summary}.


%prep
%autosetup -n %{kodi_addon}-%{version}-%{kodi_codename} -p1


%build
%cmake3 \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
%cmake3_build


%install
%cmake3_install
mkdir -p %{buildroot}/%{_datadir}/licenses/%{name}
cp -p %{SOURCE1} %{buildroot}/%{_datadir}/licenses/%{name}/LICENSE.md


%files
%doc README.md %{kodi_addon}/changelog.txt
%license LICENSE.md
%{_libdir}/kodi/addons/%{kodi_addon}/
%{_datadir}/kodi/addons/%{kodi_addon}/


%changelog
* Tue Nov 03 2020 Michael Cronenworth <mike@cchtml.com> - 3.4.3-1
- Initial RPM release
