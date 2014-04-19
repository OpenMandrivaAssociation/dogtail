Summary: GUI test tool and automation framework
Name: dogtail
Version: 0.9.0
Release: 1
License: GPLv2
Group: System/X11
URL: https://fedorahosted.org/dogtail/
Source0: https://fedorahosted.org/released/dogtail/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: imagemagick
BuildArch: noarch
BuildRequires: python-devel
BuildRequires: desktop-file-utils
Requires: python-rpm
Requires: python-at-spi
Requires: python-imaging
Requires: pygtk2.0-libglade
Requires: python-gi
Requires: python-cairo

%description
GUI test tool and automation framework that uses Accessibility (a11y) 
technologies to communicate with desktop applications.

%prep
%setup -q

%build
python ./setup.py build

%install
python ./setup.py install -O2 --root=%{buildroot} 

rm -fr %{buildroot}%{_datadir}/doc/dogtail

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
convert -resize 16x16 icons/dogtail-head-48.png %buildroot%{_iconsdir}/hicolor/16x16/apps/dogtail-head.png
convert -resize 32x32 icons/dogtail-head-48.png %buildroot%{_iconsdir}/hicolor/32x32/apps/dogtail-head.png
convert -resize 48x48 icons/dogtail-head-48.png %buildroot%{_iconsdir}/hicolor/48x48/apps/dogtail-head.png

%files 
%doc COPYING examples NEWS
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/dogtail
%{py_puresitedir}/dogtail
%{py_puresitedir}/*.egg-info
%{_iconsdir}/hicolor/*/apps/*

