#
%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_rubylibdir	%(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby Class Browser
Name:		rbbr
Version:	0.4.0
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/ruby-gnome2/%{name}-%{version}-withapi.tar.gz
# Source0-md5:	7e8ebe379414194f0f9680810bf346c2
URL:		http://ruby-gnome2.sourceforge.jp/hiki.cgi?rbbr
BuildRequires:	ruby
BuildArch:	noarch
Requires:	ruby
Requires: ruby-gnome2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class Browser written in Ruby with Gnome2

%prep
%setup -q -n %{name}-%{version}-withapi

ruby install.rb config \
	--std-ruby=%{ruby_rubylibdir} \
	--site-ruby=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

%build
ruby install.rb setup


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}
install -d $RPM_BUILD_ROOT%{_bindir}
ruby install.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README README.ja ChangeLog
%attr(755,root,root) %{_bindir}/*
%{ruby_rubylibdir}/*.rb
%{ruby_rubylibdir}/%{name}
%{_datadir}/%{name}
