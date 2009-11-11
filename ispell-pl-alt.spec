Summary:	An alternative Polish dictionary for ispell by kurnik.pl
Summary(pl.UTF-8):	Alternatywny polski słownik dla ispella autorstwa kurnik.pl
Name:		ispell-pl-alt
Version:	20091110
Release:	1
License:	Creative Commons License (see COPYING)
Group:		Applications/Text
Source0:	http://sjp.pl/slownik/ort/sjp-ispell-pl-%{version}-src.tar.bz2
# Source0-md5:	299e9827e9817779bb3d7e533c96d3a0
Source1:	http://creativecommons.org/licenses/sa/1.0/legalcode
URL:		http://www.kurnik.pl/slownik/ort/
BuildRequires:	ispell >= 3.2.06
Requires:	ispell >= 3.2.06
Obsoletes:	ispell-polish
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Alternative Polish dictionary for ispell, done for gaming purposes
initially, at the moment contains 2,9 million words and has one of the
best grammatic rules.

Visit http://www.kurnik.pl/ once in awhile.

%description -l pl.UTF-8
Alternatywny polski słownik dla programu ispell, na początku tworzony
do gier ortograficznych, z czasem przerodził się w jeden z
największych (2,9 mln. słów), najlepiej ubogaconych (m.in. w zasady
gramatyczne) oraz najszybciej rozwijanych.

Zapraszamy na <http://www.kurnik.pl/>.

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
%{_libdir}/ispell/*
