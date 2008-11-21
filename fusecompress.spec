%define	tag	2a6dff0dc32c4c93cc08b2ba224bf9ef8e2485b4
Summary:	Transparent read-write compression filesystem
Summary(pl.UTF-8):	System plików z przezroczystą kompresją danych
Name:		fusecompress
Version:	2.0
Release:	0.1
License:	GPL
Group:		Applications/System
# http://github.com/tex/fusecompress/tree/master
Source0:	tex-fusecompress-%{tag}.tar.gz
# Source0-md5:	a0b2d0b3266e604fb4684a658aa0d87e
Patch0:		%{name}-build.patch
URL:		http://miio.net/fusecompress/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	boost-devel
BuildRequires:	bzip2-devel
BuildRequires:	libfuse-devel
BuildRequires:	libmagic-devel
BuildRequires:	lzma-devel
BuildRequires:	libstdc++-devel
BuildRequires:	rlog-devel >= 1.3
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FuseCompress provides a mountable Linux filesystem which transparently
compress its content. Files stored in this filesystem are compressed
on the fly and Fuse allows to create a transparent interface between
compressed files and user applications.

%description -l pl.UTF-8
FuseCompress udostępnia montowalny system plików, który przezroczyście
kompresuje swoją zawartość. Pliki przechowywane na tym systemie plików
są kompresowane w locie, a Fuse pozwala utworzyć przezroczysty
interfejs między skompresowanymi plikami a aplikacjami użytkownika

%prep
%setup -q -n tex-%{name}-%{tag}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}_offline
%{_mandir}/man1/*.1*
