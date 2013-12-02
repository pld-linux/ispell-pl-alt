Summary:	SJP.pl Polish dictionary for ispell
Summary(pl.UTF-8):	Słownik polski SJP.pl dla ispella
Name:		ispell-pl-alt
Version:	20131202
Release:	1
License:	Creative Commons License (see COPYING)
Group:		Applications/Text
Source0:	http://sjp.pl/slownik/ort/sjp-ispell-pl-%{version}-src.tar.bz2
# Source0-md5:	4242c84459a30ede4d8577978ee74ce9
Source1:	http://creativecommons.org/licenses/sa/1.0/legalcode
URL:		http://www.sjp.pl/slownik/ort/
BuildRequires:	ispell >= 3.2.06
Requires:	ispell >= 3.2.06
Obsoletes:	ispell-polish
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SJP.pl (formerly called "alternative") Polish dictionary for ispell,
done for gaming purposes initially, at the moment contains 2.9 million
words and has one of the best grammatic rules.

%description -l pl.UTF-8
Słownik polski SJP.pl (dawniej znany jako "alternatywny") dla programu
ispell, na początku tworzony do gier ortograficznych, z czasem
przerodził się w jeden z największych (2,9 mln. słów), najlepiej
ubogaconych (m.in. w zasady gramatyczne) oraz najszybciej rozwijanych
słowników.

%prep
%setup -q -n sjp-ispell-pl-%{version}

%build
./build A *

cp %{SOURCE1} ./legalcode.html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ispell

install polish.aff $RPM_BUILD_ROOT%{_libdir}/ispell/polish-alt.aff
install polish.hash $RPM_BUILD_ROOT%{_libdir}/ispell/polish-alt.hash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README legalcode.html
%{_libdir}/ispell/polish-alt.*
