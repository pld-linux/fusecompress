%define	tag	c5e5eb58e48a6ad08298f178a9d91b9539abf883
Summary:	Transparent read-write compression filesystem
Summary(pl.UTF-8):	System plików z przezroczystą kompresją danych
Name:		fusecompress
Version:	2.2
Release:	0.1
License:	GPL
Group:		Applications/System
# http://github.com/tex/fusecompress/tree/master
Source0:	tex-fusecompress-%{tag}.tar.gz
# Source0-md5:	733fcf027b7d030d659bbb655c527999
Patch0:		%{name}-boost.patch
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
%{__aclocal} -I m4
%{__autoconf}
%configure \
	--with-boost-libdir=%{_libdir} \
	--with-boost-serialization=boost_serialization \
	--with-boost-iostreams=boost_iostreams \
	--with-boost-program-options=boost_program_options \
	--with-boost-filesystem=boost_filesystem \
	--with-lzma \
	--with-z \
	--with-bz2 \
	--with-lzo2
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/{print_compress,fusecompress_print_compress}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%attr(755,root,root) %{_bindir}/%{name}_offline
%attr(755,root,root) %{_bindir}/%{name}_print_compress
%{_mandir}/man1/*.1*
