Summary: GUI test tool and automation framework
Name: dogtail
Version: 0.6.1
Release: %mkrel 3
License: GPL
Group: System/X11
URL: http://people.redhat.com/zcerza/dogtail/
Source0: http://people.redhat.com/zcerza/%name/releases/%{name}-%{version}.tar.gz
Patch0: dogtail-0.6.1-desktop-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ImageMagick
BuildArch: noarch
%py_requires -d
Requires: x11-server-xvfb

%description
GUI test tool and automation framework that uses Accessibility (a11y) 
technologies to communicate with desktop applications.

%prep
%setup -q
%patch0 -p0

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install -O2 --root=$RPM_BUILD_ROOT 

rm -fr $RPM_BUILD_ROOT%{_datadir}/doc/dogtail

mkdir -p $RPM_BUILD_ROOT%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -resize 16x16 icons/dogtail-head-48.png %buildroot%{_iconsdir}/hicolor/16x16/apps/dogtail-head.png
convert -resize 32x32 icons/dogtail-head-48.png %buildroot%{_iconsdir}/hicolor/32x32/apps/dogtail-head.png
convert -resize 48x48 icons/dogtail-head-48.png %buildroot%{_iconsdir}/hicolor/48x48/apps/dogtail-head.png

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%update_icon_cache hicolor

%postun
%{clean_menus}
%clean_icon_cache hicolor

%files 
%defattr(-,root,root,-)
%doc COPYING examples
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/dogtail
%{py_puresitedir}/dogtail
%{py_puresitedir}/*.egg-info
%{_iconsdir}/hicolor/*/apps/*
