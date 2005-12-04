Summary:	Grabs a frame from the videodevice
Summary(pl):	Pobiera ramkê obrazu z urz±dzenia wideo
Name:		vgrabbj
Version:	0.9.6
Release:	1
License:	GPL
Group:		Applications
Source0:	http://vgrabbj.gecius.de/vgrabbj/%{name}-%{version}.tar.gz
# Source0-md5:	be12a7fdd1b80de4f74d637c2bc87099
URL:		http://vgrabbj.gecius.de
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
vgrabbj grabs a frame from the videodevice and writes it as a JPG/PNG
to stdout or a file, which makes it ideal for a Web cam. It supports
timestamping, can run as daemon, and shows the current settings of a
video device.

%description -l pl
vgrabbj pobiera ramkê z urz±dzenia video i zapisuje j± jako JPG/PNG na
standardowe wyj¶cie lub do pliku, co jest idealne dla kamery
internetowej. Posiada mo¿liwo¶æ do³±czenia aktualnej daty, pracy jako
us³uga oraz pokazywania aktualnych ustawieñ urz±dzenia wideo.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-ftp
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS TODO vgrabbj.conf.default
%attr(755,root,root) %{_bindir}/vgrabbj
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/vgrabbj.*
%{_mandir}/man5/vgrabbj.*
