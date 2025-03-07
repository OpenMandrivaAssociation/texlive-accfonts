Name:		texlive-accfonts
Version:	18835
Release:	2
Summary:	Utilities to derive new fonts from existing ones
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/utilities/accfonts
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accfonts.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/accfonts.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-accfonts.bin = %{EVRD}

%description
The accfonts package contains three utilities to permit easy
manipulation of fonts, in particular the creation of unusual
accented characters. Mkt1font works on Adobe Type 1 fonts,
vpl2vpl works on TeX virtual fonts and vpl2ovp transforms a TeX
font to an Omega one. All three programs read in a font (either
the font itself or a property list), together with a simple
definition file containing lines such as '128 z acute'; they
then write out a new version of the font with the requested new
characters in the numerical slots specified. Great care is
taken over the positioning of accents, and over the provision
of kerning information for new characters; mkt1font also
generates suitable "hints" to enhance quality at small sizes or
poor resolutions. The programs are written in Perl.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/mkt1font
%{_bindir}/vpl2ovp
%{_bindir}/vpl2vpl
%{_texmfdistdir}/scripts/accfonts/mkt1font
%{_texmfdistdir}/scripts/accfonts/vpl2ovp
%{_texmfdistdir}/scripts/accfonts/vpl2vpl
%{_texmfdistdir}/tex/latex/accfonts/CSX.def
%{_texmfdistdir}/tex/latex/accfonts/ISO-Latin1.def
%{_texmfdistdir}/tex/latex/accfonts/ISO-Latin2.def
%{_texmfdistdir}/tex/latex/accfonts/IndUni_Omega.def
%{_texmfdistdir}/tex/latex/accfonts/Norman.def
%doc %{_texmfdistdir}/doc/fonts/accfonts/CHANGES
%doc %{_texmfdistdir}/doc/fonts/accfonts/COPYING
%doc %{_texmfdistdir}/doc/fonts/accfonts/README

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/accfonts/mkt1font mkt1font
ln -sf %{_texmfdistdir}/scripts/accfonts/vpl2ovp vpl2ovp
ln -sf %{_texmfdistdir}/scripts/accfonts/vpl2vpl vpl2vpl
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
