Name:		chemical-mime-data
Version:	0.1.94
Release:	8
Summary:	Support for chemical/* MIME types
Group:		System/Libraries
License:	LGPLv2.1
URL:		http://sourceforge.net/projects/chemical-mime/
Source0:	http://dl.sourceforge.net/chemical-mime/%{name}-%{version}.tar.bz2
Patch0:		chemical-mime-data-0.1.94-rosa-rsvg.patch
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	intltool
BuildRequires:	librsvg
BuildRequires:	libxslt-proc
BuildRequires:	shared-mime-info
Requires:	pkgconfig
Requires:	shared-mime-info
Requires:	hicolor-icon-theme
BuildArch:	noarch

%description
A collection of data files which tries to give support for various chemical
MIME types (chemical/*) on Linux/UNIX desktops. Chemical MIME's have been
proposed in 1995, though it seems they have never been registered with IANA.

%prep
%setup -q
sed -i -e '/^libdir/d' chemical-mime-data.pc.in
%patch0 -p1

%build
# required for patch0
autoreconf

export RSVG=%{_bindir}/rsvg-convert
%configure --disable-update-database \
           --without-gnome-mime \
           --without-pixmaps
%make

%install
make INSTALL="install -p" install DESTDIR=%{buildroot}
cp -pR %{buildroot}%{_docdir}/%{name} __docs
rm -rf %{buildroot}%{_docdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING HACKING NEWS README THANKS TODO
%doc __docs/*
%{_datadir}/icons/hicolor/*/mimetypes/gnome-mime-chemical.png
%{_datadir}/icons/hicolor/scalable/mimetypes/gnome-mime-chemical.svgz
%{_datadir}/mime/packages/chemical-mime-data.xml
%{_datadir}/mimelnk
%{_datadir}/pkgconfig/chemical-mime-data.pc

