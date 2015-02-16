%define	tag	c5e5eb58e48a6ad08298f178a9d91b9539abf883
Summary:	Transparent read-write compression filesystem
Summary(pl.UTF-8):	System plików z przezroczystą kompresją danych
Name:		fusecompress
Version:	2.6
Release:	8
License:	GPL v2+
Group:		Applications/System
Source0:	https://github.com/tex/fusecompress/archive/2.6.tar.gz
# Source0-md5:	923688bd13b9d87fb74a0449bdf86724
Patch0:		fusecompress-git.patch
URL:		https://code.google.com/p/fusecompress/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	boost-devel >= 1.33.1
BuildRequires:	bzip2-devel
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libmagic-devel
BuildRequires:	lzo-devel >= 2
BuildRequires:	libstdc++-devel
BuildRequires:	rlog-devel >= 1.3
BuildRequires:	xz-devel
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
%setup -q -n %{name}-%{version}
%patch0 -p1

# gold causes really weird issues with fuse apps
install -d ld-dir
[ ! -x /usr/bin/ld.bfd ] || ln -sf /usr/bin/ld.bfd ld-dir/ld

%build
PATH=$(pwd)/ld-dir:$PATH
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--bindir=%{_sbindir} \
	--with-boost-libdir=%{_libdir} \
	--with-boost-filesystem=boost_filesystem \
	--with-boost-iostreams=boost_iostreams \
	--with-boost-program-options=boost_program_options \
	--with-boost-serialization=boost_serialization \
	--with-boost-system=boost_system \
	--with-bz2 \
	--with-lzma \
	--with-lzo2 \
	--with-z
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__mv} $RPM_BUILD_ROOT%{_sbindir}/{print_compress,fusecompress_print_compress}
%{__rm} $RPM_BUILD_ROOT%{_sbindir}/xattrs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE NEWS README TODO
%attr(755,root,root) %{_sbindir}/mount.fusecompress
%attr(755,root,root) %{_sbindir}/%{name}
%attr(755,root,root) %{_sbindir}/%{name}_offline
%attr(755,root,root) %{_sbindir}/%{name}_print_compress
%{_mandir}/man1/fusecompress.1*
%{_mandir}/man1/fusecompress_offline.1*
