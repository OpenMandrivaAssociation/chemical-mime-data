Name:           chemical-mime-data
Version:        0.1.94
Release:        7
Summary:        Support for chemical/* MIME types

Group:          System/Libraries
License:        LGPLv2.1
URL:            http://sourceforge.net/projects/chemical-mime/
Source0:        http://dl.sourceforge.net/chemical-mime/%{name}-%{version}.tar.bz2
Patch0:		chemical-mime-data-0.1.94-rosa-rsvg.patch
BuildArch:      noarch
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  shared-mime-info
BuildRequires:  pkgconfig
BuildRequires:  intltool
BuildRequires:  gettext-devel
BuildRequires:  libxslt-proc
BuildRequires:	librsvg
BuildRequires:	pkgconfig(librsvg-2.0)
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





%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.94-6mdv2011.0
+ Revision: 617000
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.1.94-5mdv2010.0
+ Revision: 424829
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.1.94-4mdv2009.0
+ Revision: 243875
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.1.94-2mdv2008.1
+ Revision: 140692
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Mon Mar 05 2007 Nicolas Lécureuil <neoclust@mandriva.org> 0.1.94-2mdv2007.1
+ Revision: 132761
- Fix group

* Sun Feb 25 2007 Emmanuel Andry <eandry@mandriva.org> 0.1.94-1mdv2007.1
+ Revision: 125468
- buildrequires librsvg
- buildrequires libxslt-proc
- Import chemical-mime-data

