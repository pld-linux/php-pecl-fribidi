%define		_modname	fribidi
%define		_status		stable
Summary:	%{_modname} - Implementation of the Unicode BiDi algorithm
Summary(pl):	%{_modname} - Implementacja algorytmu BiDi Unicode
Name:		php-pecl-%{_modname}
Version:	1.0
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	360e55f049cdebc96fe797eba78399ef
URL:		http://pecl.php.net/package/fribidi/
BuildRequires:	fribidi-devel
BuildRequires:	libtool
BuildRequires:	php-devel
Requires:	php-common
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
A PHP frontend to the FriBidi library: an implemntation of the unicode
Bidi algorithm, provides means of handling right-to-left text.

In PECL status of this package is: %{_status}.

%description -l pl
Frontend PHP do biblioteki FriBidi: implementacji algorytmu unicode
Bidi, dostarczaj±cego ¶rodki do obs³ugi tekstu pisanego od prawej do
lewej.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
