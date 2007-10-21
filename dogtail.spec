Summary: GUI test tool and automation framework
Name: dogtail
Version: 0.6.1
Release: %mkrel 1
License: GPL
Group: System/X11
URL: http://people.redhat.com/zcerza/dogtail/
Source0: http://people.redhat.com/zcerza/%name/releases/%{name}-%{version}.tar.gz
Patch0: dogtail-0.6.1-desktop-fix.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
%py_requires -d
Requires: xorg-x11-Xvfb

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

mkdir -p $RPM_BUILD_ROOT%{_menudir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
%update_icon_cache hiclor

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
