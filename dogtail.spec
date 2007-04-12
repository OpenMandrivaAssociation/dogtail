Summary: GUI test tool and automation framework
Name: dogtail
Version: 0.6.0
Release: %mkrel 1
License: GPL
Group: System/X11
URL: http://people.redhat.com/zcerza/dogtail/
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArchitectures: noarch
BuildRequires: python-devel desktop-file-utils
Requires: xorg-x11-Xvfb

%description
GUI test tool and automation framework that uses Accessibility (a11y) 
technologies to communicate with desktop applications.

%prep
%setup -q

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python ./setup.py install -O2 --root=$RPM_BUILD_ROOT 

rm -fr $RPM_BUILD_ROOT%{_datadir}/doc/dogtail

mkdir -p $RPM_BUILD_ROOT%{_menudir}

cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_bindir}/sniff" \
needs="gnome" section="More Applications/Accessibility" title="AT-SPI Browser" \
longtitle="Browse your Assistive Technology-enabled desktop" icon="dogtail-head-48.png" \
xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Utility" \
  --add-category="Accessibility" \
  --add-category="X-MandrivaLinux-MoreApplications-Accessibility" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}
gtk-update-icon-cache --force --quiet %{_datadir}/icons/hicolor

%postun
%{clean_menus}
gtk-update-icon-cache --force --quiet %{_datadir}/icons/hicolor

%files 
%defattr(-,root,root,-)
%doc COPYING examples
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/dogtail
%{py_puresitedir}/dogtail
%{py_puresitedir}/*.egg-info
%{_menudir}/*
%{_iconsdir}/hicolor/*/apps/*


