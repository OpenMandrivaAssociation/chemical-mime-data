Name:           chemical-mime-data
Version:        0.1.94
Release:        %mkrel 5
Summary:        Support for chemical/* MIME types

Group:          System/Libraries
License:        LGPL
URL:            http://sourceforge.net/projects/chemical-mime/
Source0:        http://dl.sourceforge.net/chemical-mime/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-buildroot
BuildArch:      noarch
BuildRequires:  perl(XML::Parser)
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  librsvg2-devel
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig
BuildRequires:  intltool
BuildRequires:  gettext-devel
BuildRequires:  libxslt-proc
BuildRequires:	librsvg
Requires:       pkgconfig
Requires:       shared-mime-info
Requires:       hicolor-icon-theme

%description
A collection of data files which tries to give support for various chemical
MIME types (chemical/*) on Linux/UNIX desktops. Chemical MIME's have been
proposed in 1995, though it seems they have never been registered with IANA.


%prep
%setup -q
sed -i -e '/^libdir/d' chemical-mime-data.pc.in


%build
%configure --disable-update-database \
           --without-gnome-mime \
           --without-pixmaps
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make INSTALL="install -p" install DESTDIR=$RPM_BUILD_ROOT
cp -pR $RPM_BUILD_ROOT%{_docdir}/%{name} __docs
rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}

%find_lang %{name}

%post
update-mime-database %{_datadir}/mime &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
update-mime-database %{_datadir}/mime &> /dev/null || :
touch --no-create %{_datadir}/icons/hicolor || :
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%clean
rm -rf $RPM_BUILD_ROOT


%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING HACKING NEWS README THANKS TODO
%doc __docs/*
%{_datadir}/icons/hicolor/*/mimetypes/gnome-mime-chemical.png
%{_datadir}/icons/hicolor/scalable/mimetypes/gnome-mime-chemical.svgz
%{_datadir}/mime/packages/chemical-mime-data.xml
%{_datadir}/mimelnk
%{_datadir}/pkgconfig/chemical-mime-data.pc



