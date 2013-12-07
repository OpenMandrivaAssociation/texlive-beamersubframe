# revision 23510
# category Package
# catalog-ctan /macros/latex/contrib/beamer-contrib/beamersubframe
# catalog-date 2011-08-11 10:23:40 +0200
# catalog-license lppl
# catalog-version 0.2
Name:		texlive-beamersubframe
Version:	0.2
Release:	6
Summary:	Reorder frames in the PDF file
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/beamer-contrib/beamersubframe
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamersubframe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamersubframe.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/beamersubframe.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a method to reorder frames in the PDF file
without reordering the source. Its principal use is to embed or
append frames with details on some subject. The author
describes the package as "experimental".

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/beamersubframe/beamersubframe.sty
%doc %{_texmfdistdir}/doc/latex/beamersubframe/README
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-append.pdf
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-append.svg
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-embed.pdf
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe-embed.svg
%doc %{_texmfdistdir}/doc/latex/beamersubframe/beamersubframe.pdf
%doc %{_texmfdistdir}/doc/latex/beamersubframe/bsf-example.tex
#- source
%doc %{_texmfdistdir}/source/latex/beamersubframe/beamersubframe.dtx
%doc %{_texmfdistdir}/source/latex/beamersubframe/beamersubframe.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 749531
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 717899
- texlive-beamersubframe
- texlive-beamersubframe
- texlive-beamersubframe
- texlive-beamersubframe
- texlive-beamersubframe

