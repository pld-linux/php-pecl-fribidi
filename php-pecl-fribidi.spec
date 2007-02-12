%define		_modname	fribidi
%define		_status		stable
Summary:	%{_modname} - Implementation of the Unicode BiDi algorithm
Summary(pl.UTF-8):	%{_modname} - Implementacja algorytmu BiDi Unicode
Name:		php-pecl-%{_modname}
Version:	1.0
Release:	7
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	360e55f049cdebc96fe797eba78399ef
URL:		http://pecl.php.net/package/fribidi/
BuildRequires:	fribidi-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-fribidi
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A PHP frontend to the FriBidi library: an implemntation of the unicode
Bidi algorithm, provides means of handling right-to-left text.

In PECL status of this package is: %{_status}.

%description -l pl.UTF-8
Frontend PHP do biblioteki FriBidi: implementacji algorytmu unicode
Bidi, dostarczającego środki do obsługi tekstu pisanego od prawej do
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
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so
