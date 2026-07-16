#!/usr/bin/env python3
"""Generate the complete Applettek multi-page website under website/."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent

TAILWIND = """
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            primary: { DEFAULT: '#F04C23', 100: '#ea3b10', soft: '#f25f3b' },
            secondary: '#FF6037',
            tertiary: '#DC380F',
            quaternary: '#383F48',
            dark: '#212529',
            grey: { DEFAULT: '#777', light: '#F4F4F4', soft: '#F3F3F3', mid: '#5a6267', border: '#404040' }
          },
          fontFamily: { sans: ['Poppins', 'sans-serif'] },
          boxShadow: {
            card: '0 0 40px 0 rgba(187, 187, 187, 0.3)',
            soft: '0 12px 40px rgba(0,0,0,0.08)',
            img: '0 10px 30px rgba(0,0,0,0.12)',
          },
          maxWidth: { container: '1140px' }
        }
      }
    }
  </script>
"""


def page_shell(title, description, page_id, base, body, extra_head=""):
    fav = f"{base}assets/brand/logos/favicon.png"
    css = f"{base}css/site.css"
    js = f"{base}js/site.js"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{description}" />
  <link rel="icon" href="{fav}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css" />
  {TAILWIND}
  <link rel="stylesheet" href="{css}" />
  {extra_head}
</head>
<body class="bg-white antialiased" data-base="{base}" data-page="{page_id}">
  <div id="site-header"></div>
  <main>
{body}
  </main>
  <div id="site-footer"></div>
  <script src="{js}"></script>
</body>
</html>
"""


def page_hero(base, title, breadcrumb, bg="assets/theme/backgrounds/background-1.jpg"):
    return f"""
    <section class="page-hero relative py-20 md:py-28 text-white" style="background-image: linear-gradient(rgba(33,37,41,0.75), rgba(33,37,41,0.75)), url('{base}{bg}');">
      <div class="max-w-container mx-auto px-4 relative z-[1]">
        <p class="text-sm font-medium tracking-wider text-primary mb-3">{breadcrumb}</p>
        <h1 class="text-4xl md:text-5xl font-semibold text-white">{title}</h1>
      </div>
    </section>
"""


def write(rel_path, content):
    path = ROOT / rel_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print("Wrote", rel_path)


# ── Homepage ──────────────────────────────────────────────────────────────

def homepage():
    base = ""
    b = lambda p: base + p
    body = f"""
    <!-- HERO -->
    <section class="relative overflow-hidden border-0 m-0 bg-cover bg-center bg-no-repeat" style="background-image: url('{b('assets/brand/images/slider-1ap.jpg')}');">
      <div class="absolute inset-0 bg-gradient-to-r from-white/95 via-white/80 to-white/30"></div>
      <div class="relative max-w-container mx-auto px-4 pb-40 md:pb-52 pt-16 md:pt-20">
        <div class="fade-up">
          <h1 class="text-clip-bg text-[2.5rem] sm:text-5xl xl:text-[5.5rem] font-bold leading-none pb-2 mb-6 xl:mb-10"
              style="background-image: url('{b('assets/theme/backgrounds/text-background.jpg')}');">
            IT CONSULTING
          </h1>
        </div>
        <div class="max-w-xl pb-16 md:pb-24 fade-up">
          <strong class="block font-semibold text-dark text-xl md:text-2xl leading-snug mb-4">
            Drive growth with our <span class="highlight-underline font-bold">strategic IT consulting services</span>
          </strong>
          <p class="text-base md:text-lg mb-6 leading-relaxed">
            Consulting Business can transform quickly. We help organizations leverage technology to address business challenges and improve efficiency.
          </p>
          <div class="flex flex-wrap gap-4">
            <a href="about-us.html" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3 text-base"><span>More About Us</span></a>
            <a href="contact-us.html" class="btn-offset inline-flex bg-dark text-white font-semibold px-6 py-3 text-base"><span>Contact Us</span></a>
          </div>
        </div>
      </div>
      <div class="shape-bottom absolute bottom-0 left-0 w-full h-[120px] md:h-[180px] pointer-events-none">
        <svg viewBox="0 0 1920 212" preserveAspectRatio="none" class="w-full h-full">
          <polygon fill="#F3F3F3" points="0,75 479,161 1357,28 1701,56 1920,26 1920,213 0,212" />
          <polygon fill="#FFFFFF" points="0,91 481,177 1358,44 1702,72 1920,42 1920,212 0,212" />
        </svg>
      </div>
    </section>

    <!-- FEATURE CARDS -->
    <div class="relative z-10 max-w-container mx-auto px-4" style="margin-top: -160px;">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
        <a href="services/erp-services.html" class="link-hover block bg-white shadow-card text-center py-10 px-6 hover:shadow-soft transition">
          <img src="{b('assets/theme/icons/primary-blackboard.svg')}" alt="" class="w-[75px] h-[75px] mx-auto mb-2" />
          <div class="crooked mx-auto mb-3"><img src="{b('assets/theme/icons/primary-infinite-crooked-line.svg')}" alt="" class="w-[154px] h-[26px] max-w-none" /></div>
          <h2 class="text-xl font-semibold text-dark mb-2">ERP Services</h2>
          <p class="text-sm mb-3">Streamline and integrate back-office business processes with proven ERP software solutions.</p>
          <span class="view-arrow inline-flex items-center gap-1 font-medium text-primary">View More <img src="{b('assets/theme/icons/primary-arrow-right.svg')}" alt="" class="w-[27px]" /></span>
        </a>
        <a href="services/application-managed-services.html" class="link-hover block bg-white shadow-card text-center py-10 px-6 hover:shadow-soft transition">
          <img src="{b('assets/theme/icons/primary-weight-balance.svg')}" alt="" class="w-[75px] h-[75px] mx-auto mb-2" />
          <div class="crooked mx-auto mb-3"><img src="{b('assets/theme/icons/primary-infinite-crooked-line.svg')}" alt="" class="w-[154px] h-[26px] max-w-none" /></div>
          <h2 class="text-xl font-semibold text-dark mb-2">Application Managed Services</h2>
          <p class="text-sm mb-3">Leveraging proven methodology and automated tools for reliable application management.</p>
          <span class="view-arrow inline-flex items-center gap-1 font-medium text-primary">View More <img src="{b('assets/theme/icons/primary-arrow-right.svg')}" alt="" class="w-[27px]" /></span>
        </a>
        <a href="services/web-development.html" class="link-hover block bg-white shadow-card text-center py-10 px-6 hover:shadow-soft transition sm:col-span-2 lg:col-span-1">
          <img src="{b('assets/theme/icons/primary-blackboard.svg')}" alt="" class="w-[75px] h-[75px] mx-auto mb-2" />
          <div class="crooked mx-auto mb-3"><img src="{b('assets/theme/icons/primary-infinite-crooked-line.svg')}" alt="" class="w-[154px] h-[26px] max-w-none" /></div>
          <h2 class="text-xl font-semibold text-dark mb-2">Web Development</h2>
          <p class="text-sm mb-3">Decade-long experience developing web-based solutions that strengthen your business.</p>
          <span class="view-arrow inline-flex items-center gap-1 font-medium text-primary">View More <img src="{b('assets/theme/icons/primary-arrow-right.svg')}" alt="" class="w-[27px]" /></span>
        </a>
      </div>

      <!-- ABOUT -->
      <div id="aboutus" class="grid lg:grid-cols-2 gap-10 xl:gap-16 items-center pt-16 md:pt-24 pb-8">
        <div class="grid grid-cols-2 gap-3 fade-up">
          <div><img src="{b('assets/brand/images/about-3.jpg')}" alt="" class="w-full shadow-img h-full object-cover" /></div>
          <div class="flex flex-col gap-3">
            <img src="{b('assets/brand/images/about-4.jpg')}" alt="" class="w-full shadow-img" />
            <img src="{b('assets/theme/generic/generic-3.jpg')}" alt="" class="w-full shadow-img" />
          </div>
        </div>
        <div class="fade-up">
          <h2 class="highlight-underline text-primary text-sm font-medium tracking-[0.15em] mb-3">ABOUT US</h2>
          <h3 class="text-dark text-3xl md:text-4xl font-semibold leading-snug mb-5">IT consulting Services</h3>
          <p class="text-base md:text-lg mb-8 leading-relaxed">
            IT consulting services encompass a wide range of expertise and assistance in leveraging technology to address business challenges and improve organizational efficiency. IT consultants offer guidance in areas such as technology strategy, system implementation and integration, cybersecurity, data management, cloud computing, digital transformation, and more. They collaborate with clients to analyze their specific needs, identify opportunities for improvement, design tailored solutions, and provide implementation support.
          </p>
          <a href="about-us.html" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3 text-base"><span>Read More</span></a>
        </div>
      </div>
    </div>

    <!-- CLIENT LOGOS -->
    <div class="py-12 md:py-16 overflow-hidden">
      <div class="flex flex-wrap justify-center items-center gap-10 md:gap-16 px-4 opacity-80">
        <img src="{b('assets/brand/clients/citi-logo-11.png')}" alt="Citi" class="max-h-[48px] w-auto max-w-[140px] object-contain" />
        <img src="{b('assets/brand/clients/lowes-logo-11.png')}" alt="Lowe's" class="max-h-[48px] w-auto max-w-[140px] object-contain" />
        <img src="{b('assets/brand/images/company.png')}" alt="Client" class="max-h-[48px] w-auto max-w-[120px] object-contain" />
        <img src="{b('assets/brand/images/erp-logos.png')}" alt="ERP partners" class="max-h-[48px] w-auto max-w-[160px] object-contain" />
      </div>
    </div>

    <!-- SERVICES -->
    <section id="services" class="relative bg-grey-light pt-20 pb-16 md:pb-24">
      <div class="shape-top absolute top-0 left-0 w-full h-[80px] md:h-[100px] -mt-px">
        <svg viewBox="0 0 1920 123" preserveAspectRatio="none" class="w-full h-full">
          <polygon fill="#F4F4F4" points="0,90 221,60 563,88 931,35 1408,93 1920,41 1920,-1 0,-1" />
          <polygon fill="#FFFFFF" points="0,75 219,44 563,72 930,19 1408,77 1920,25 1920,-1 0,-1" />
        </svg>
      </div>
      <div class="max-w-container mx-auto px-4 relative z-[1]">
        <div class="text-center max-w-3xl mx-auto mb-12 fade-up">
          <h2 class="highlight-underline text-primary text-sm font-medium tracking-[0.15em] mb-3">OUR SOLUTIONS</h2>
          <h3 class="text-dark text-3xl md:text-4xl font-semibold mb-4">Popular Services</h3>
          <p class="text-base md:text-lg leading-relaxed">We deliver tailored IT solutions that drive success, enhance efficiency, and foster innovation.</p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5 mb-10">
"""
    service_cards = [
        ("services/erp-services.html", "ERP Services", "assets/theme/services/services-1.jpg", "Streamline and integrate back-office business processes and facilitate growth."),
        ("services/application-managed-services.html", "Application Managed Services", "assets/theme/services/services-2.jpg", "Proven methodology and automated tools for application management."),
        ("services/web-development.html", "Web Development", "assets/theme/services/services-3.jpg", "Web-based solutions that meet your business needs and strengthen your brand."),
        ("services/mobile-applications.html", "Mobile Applications", "assets/theme/services/services-4.jpg", "Custom mobile applications designed for performance and user experience."),
        ("services/qa-testing.html", "QA & Testing", "assets/theme/services/services-5.jpg", "Quality assurance and testing to ensure reliable, production-ready software."),
        ("practices/workday.html", "Workday Practice", "assets/theme/services/services-6.jpg", "Comprehensive Workday implementation, support, and value-add services."),
    ]
    for href, title, img, blurb in service_cards:
        body += f"""
          <a href="{href}" class="link-hover group block bg-white shadow-soft overflow-hidden">
            <div class="relative overlay-dark">
              <div class="absolute bottom-0 left-0 w-full py-3 px-4 z-10">
                <h4 class="font-semibold text-white text-xl mb-1">{title}</h4>
                <div class="crooked"><img src="{b('assets/theme/icons/primary-infinite-crooked-line.svg')}" alt="" class="w-[154px]" /></div>
              </div>
              <img src="{b(img)}" alt="{title}" class="w-full aspect-[4/3] object-cover" />
            </div>
            <div class="flex items-center gap-3 px-4 py-4">
              <p class="flex-1 text-sm mb-0">{blurb}</p>
              <img src="{b('assets/theme/icons/primary-arrow-right.svg')}" alt="" class="view-arrow w-[40px] shrink-0" />
            </div>
          </a>
"""
    body += f"""
        </div>
        <div class="text-center">
          <a href="services/erp-services.html" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3 text-base"><span>All Services</span></a>
        </div>
      </div>
    </section>

    <!-- CTA BAND -->
    <section class="relative py-16 md:py-20 bg-cover bg-center" style="background-image: linear-gradient(rgba(240,76,35,0.9), rgba(220,56,15,0.9)), url('{b('assets/brand/images/slider-ap-2.jpg')}');">
      <div class="max-w-container mx-auto px-4 text-center">
        <h2 class="text-white text-3xl md:text-4xl font-semibold mb-6">Good business planning ensure success.</h2>
        <a href="contact-us.html" class="btn-offset inline-flex bg-dark text-white font-semibold px-6 py-3 text-base"><span>Request Quote</span></a>
      </div>
    </section>

    <!-- WHY US / PROCESS -->
    <section class="relative bg-dark overflow-hidden">
      <div class="shape-top absolute top-0 left-0 w-full h-[70px] md:h-[90px] z-[3]">
        <svg viewBox="0 0 1920 102" preserveAspectRatio="none" class="w-full h-full">
          <polygon fill="#F3F3F3" points="0,65 220,35 562,63 931,10 1410,68 1920,16 1920,103 0,103" />
          <polygon fill="#F4F4F4" points="0,82 219,51 562,78 931,26 1409,83 1920,32 1920,103 0,103" />
        </svg>
      </div>
      <div class="absolute top-0 left-0 h-full hidden lg:block w-[40%] overlay-primary bg-cover bg-center" style="background-image: url('{b('assets/theme/parallax/parallax-1.jpg')}');"></div>
      <div class="relative z-[2] max-w-container mx-auto px-4 pt-24 pb-20 md:pt-28 md:pb-24">
        <div class="grid lg:grid-cols-2 gap-10 items-center">
          <div class="hidden lg:block">
            <h2 class="text-clip-bg text-clip-bg-light text-[4.5rem] xl:text-[6rem] font-bold leading-none float-right pe-8"
                style="background-image: url('{b('assets/theme/backgrounds/text-background-2.jpg')}');">PROCESS</h2>
          </div>
          <div class="fade-up">
            <h2 class="highlight-underline text-primary text-sm font-medium tracking-[0.15em] mb-3">WORK PROCESS</h2>
            <h3 class="text-white text-3xl md:text-4xl font-medium leading-snug mb-5">Our Solution Process</h3>
            <p class="text-base md:text-lg text-gray-300 mb-8 leading-relaxed">A structured approach to delivering IT solutions that align with your objectives.</p>
            <ul class="space-y-5">
              <li class="flex items-start gap-4">
                <span class="shrink-0 w-11 h-11 rounded-full bg-primary flex items-center justify-center text-white font-bold text-sm">01</span>
                <span class="text-base text-gray-200 pt-2"><strong class="text-white">Initial Assessment</strong> — Consultants work closely with stakeholders to understand the organization's objectives.</span>
              </li>
              <li class="flex items-start gap-4">
                <span class="shrink-0 w-11 h-11 rounded-full bg-primary flex items-center justify-center text-white font-bold text-sm">02</span>
                <span class="text-base text-gray-200 pt-2"><strong class="text-white">Requirements Gathering</strong> — Collaborate with your IT team to gather detailed requirements.</span>
              </li>
              <li class="flex items-start gap-4">
                <span class="shrink-0 w-11 h-11 rounded-full bg-primary flex items-center justify-center text-white font-bold text-sm">03</span>
                <span class="text-base text-gray-200 pt-2"><strong class="text-white">Risk Analysis and Planning</strong> — Identify potential threats and vulnerabilities with comprehensive analysis.</span>
              </li>
              <li class="flex items-start gap-4">
                <span class="shrink-0 w-11 h-11 rounded-full bg-primary flex items-center justify-center text-white font-bold text-sm">04</span>
                <span class="text-base text-gray-200 pt-2"><strong class="text-white">Security Architecture Design</strong> — Design a robust architecture aligned with your requirements.</span>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- OFFERINGS -->
    <div class="max-w-container mx-auto px-4 py-16 md:py-24">
      <div class="grid lg:grid-cols-12 gap-12 items-center">
        <div class="lg:col-span-7 fade-up">
          <h2 class="highlight-underline text-primary text-sm font-medium tracking-[0.15em] mb-3">OUR SOLUTIONS</h2>
          <h3 class="text-dark text-3xl md:text-4xl font-semibold leading-snug mb-5">Our Comprehensive Offerings for Success</h3>
          <p class="text-base md:text-lg mb-6 leading-relaxed">
            We are dedicated to delivering tailored IT solutions that drive success, enhance efficiency, and foster innovation. Our team of experts is committed to understanding your unique needs and providing personalized solutions that meet your business goals.
          </p>
          <div class="flex flex-wrap gap-3 mb-8">
            <span class="bg-grey-light text-dark font-medium px-4 py-2 text-sm">IT Strategy and Consulting</span>
            <span class="bg-grey-light text-dark font-medium px-4 py-2 text-sm">Data Management and Analytics</span>
          </div>
          <a href="contact-us.html" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3 text-base"><span>Contact Now</span></a>
        </div>
        <div class="lg:col-span-5 fade-up">
          <img src="{b('assets/brand/images/Image-6.jpg')}" alt="" class="w-full shadow-img" />
        </div>
      </div>
    </div>

    <!-- TEAM -->
    <section id="team" class="relative bg-grey-light pt-20 pb-16 md:pb-24">
      <div class="shape-top absolute top-0 left-0 w-full h-[80px] md:h-[100px] -mt-px">
        <svg viewBox="0 0 1920 123" preserveAspectRatio="none" class="w-full h-full">
          <polygon fill="#F3F3F3" points="0,90 221,60 563,88 931,35 1408,93 1920,41 1920,-1 0,-1" />
          <polygon fill="#FFFFFF" points="0,75 219,44 563,72 930,19 1408,77 1920,25 1920,-1 0,-1" />
        </svg>
      </div>
      <div class="max-w-container mx-auto px-4 text-center mb-10 relative z-[1]">
        <h2 class="highlight-underline text-primary text-sm font-medium tracking-[0.15em] mb-3">OUR MEMBERS</h2>
        <h3 class="text-dark text-3xl md:text-4xl font-semibold mb-4">Expert Professionals</h3>
        <p class="text-base md:text-lg max-w-3xl mx-auto leading-relaxed">Meet the professionals dedicated to delivering exceptional IT solutions and services.</p>
      </div>
      <div class="max-w-container mx-auto px-4 grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
"""
    team = [
        ("Oulian Miyako", "Manager", "assets/theme/team/team-1.jpg"),
        ("Stive Stikollo", "Designer", "assets/theme/team/team-2.jpg"),
        ("Darrell Stewart", "Support Expert", "assets/theme/team/team-3.jpg"),
        ("Erika Jayne", "SEO Specialist", "assets/theme/team/team-4.jpg"),
    ]
    for name, role, img in team:
        body += f"""
        <div class="link-hover block bg-white">
          <div class="relative">
            <div class="absolute bottom-0 left-0 w-full py-3 px-4 z-10">
              <div class="crooked"><img src="{b('assets/theme/icons/primary-infinite-crooked-line.svg')}" alt="" class="w-[154px]" /></div>
            </div>
            <img src="{b(img)}" alt="{name}" class="w-full aspect-[3/4] object-cover" />
          </div>
          <div class="p-4">
            <h4 class="text-dark text-xl mb-0">{name}</h4>
            <p class="text-base mb-0">{role}</p>
          </div>
        </div>
"""
    body += f"""
      </div>
    </section>

    <!-- CONTACT TEASER -->
    <section id="contact" class="relative bg-dark overflow-hidden">
      <div class="shape-top absolute top-0 left-0 w-full h-[70px] md:h-[90px] z-[3]">
        <svg viewBox="0 0 1920 102" preserveAspectRatio="none" class="w-full h-full">
          <polygon fill="#F3F3F3" points="0,65 220,35 562,63 931,10 1410,68 1920,16 1920,103 0,103" />
          <polygon fill="#F4F4F4" points="0,82 219,51 562,78 931,26 1409,83 1920,32 1920,103 0,103" />
        </svg>
      </div>
      <div class="absolute top-0 right-0 hidden md:block h-full w-[32%] overlay-primary bg-cover bg-center" style="background-image: url('{b('assets/theme/backgrounds/background-2.jpg')}');"></div>
      <div class="relative z-[2] max-w-container mx-auto px-4 pt-24 pb-20">
        <div class="max-w-2xl fade-up">
          <h2 class="highlight-underline text-primary text-sm font-medium tracking-[0.15em] mb-3">GET IN TOUCH</h2>
          <h3 class="text-white text-3xl md:text-4xl font-medium leading-snug mb-5">Send Us a Message and Learn More About Our Services</h3>
          <p class="text-base md:text-lg text-gray-300 mb-8 leading-relaxed">We are always ready for your solution. Reach out and our team will respond promptly.</p>
          <form id="contact-form" class="space-y-4">
            <div id="form-success" class="hidden bg-green-600/20 border border-green-500 text-green-200 px-4 py-3 text-sm">
              <strong>Success!</strong> Your message has been sent to us.
            </div>
            <div id="form-error" class="hidden bg-red-600/20 border border-red-500 text-red-200 px-4 py-3 text-sm">
              <strong>Error!</strong> There was an error sending your message.
            </div>
            <input type="text" name="name" required placeholder="* Full Name" class="w-full bg-transparent border border-grey-border text-white placeholder-gray-400 px-4 py-3 text-sm focus:outline-none focus:border-primary" />
            <input type="email" name="email" required placeholder="* Email Address" class="w-full bg-transparent border border-grey-border text-white placeholder-gray-400 px-4 py-3 text-sm focus:outline-none focus:border-primary" />
            <textarea name="message" required rows="6" placeholder="* Message" class="w-full bg-transparent border border-grey-border text-white placeholder-gray-400 px-4 py-3 text-sm focus:outline-none focus:border-primary resize-y"></textarea>
            <button type="submit" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3 text-base"><span>Send Message</span></button>
          </form>
        </div>
      </div>
    </section>

    <!-- TESTIMONIALS -->
    <section class="bg-cover bg-center py-16 md:py-24" style="background-image: url('{b('assets/theme/backgrounds/background-3.jpg')}');">
      <div class="max-w-container mx-auto px-4">
        <div class="text-center mb-10 fade-up">
          <h2 class="highlight-underline text-primary text-sm font-medium tracking-[0.15em] mb-3">TESTIMONIALS</h2>
          <h3 class="text-dark text-3xl md:text-4xl font-semibold">What People Say</h3>
        </div>
        <div class="max-w-4xl mx-auto relative fade-up">
          <div class="bg-white shadow-soft px-6 md:px-16 py-10 md:py-14 relative">
            <button id="testimonial-prev" class="hidden lg:flex absolute left-0 top-1/2 -translate-y-1/2 -translate-x-1/2 w-12 h-12 items-center justify-center bg-white shadow-soft text-dark hover:text-primary" aria-label="Previous"><i class="fas fa-chevron-left"></i></button>
            <button id="testimonial-next" class="hidden lg:flex absolute right-0 top-1/2 -translate-y-1/2 translate-x-1/2 w-12 h-12 items-center justify-center bg-white shadow-soft text-dark hover:text-primary" aria-label="Next"><i class="fas fa-chevron-right"></i></button>
            <div id="testimonials">
              <div class="testimonial-slide">
                <img src="{b('assets/theme/icons/primary-left-quote.svg')}" alt="" class="w-10 h-10 mb-4" />
                <p class="text-dark text-lg md:text-xl leading-relaxed mb-6">Applettek helped us streamline our ERP processes and improve organizational efficiency. Their consultants understood our needs and delivered tailored solutions.</p>
                <p class="mb-0"><strong class="text-dark text-xl font-bold">- Client Partner</strong></p>
                <p class="text-dark mb-0">Enterprise Customer</p>
              </div>
              <div class="testimonial-slide hidden">
                <img src="{b('assets/theme/icons/primary-left-quote.svg')}" alt="" class="w-10 h-10 mb-4" />
                <p class="text-dark text-lg md:text-xl leading-relaxed mb-6">From Workday implementation to ongoing support, the Applettek team has been a reliable partner for our digital transformation journey.</p>
                <p class="mb-0"><strong class="text-dark text-xl font-bold">- IT Director</strong></p>
                <p class="text-dark mb-0">Mid-Market Customer</p>
              </div>
            </div>
            <div class="flex justify-center gap-2 mt-8 lg:hidden" id="testimonial-dots"></div>
          </div>
        </div>
      </div>
    </section>

    <!-- BLOG -->
    <div id="blog" class="max-w-container mx-auto px-4 py-16 md:py-24">
      <div class="text-center max-w-3xl mx-auto mb-12 fade-up">
        <h2 class="highlight-underline text-primary text-sm font-medium tracking-[0.15em] mb-3">FROM THE BLOG</h2>
        <h3 class="text-dark text-3xl md:text-4xl font-semibold mb-4">News &amp; Articles</h3>
        <p class="text-base md:text-lg leading-relaxed">Insights and updates from the Applettek team.</p>
      </div>
      <div class="grid md:grid-cols-3 gap-6">
"""
    blogs = [
        ("blog/our-consultants-can-make-your-brand-a-reality.html", "18", "Our consultants can make your brand a reality", "assets/theme/blog/blog-1.jpg"),
        ("blog/when-a-small-business-is-just-starting-out.html", "16", "When a small business is just starting out", "assets/theme/blog/blog-2.jpg"),
        ("blog/finances-and-accounting-are-one-of-the-hardest.html", "16", "Finance and account are one of hardest", "assets/theme/blog/blog-3.jpg"),
    ]
    for href, day, title, img in blogs:
        body += f"""
        <a href="{href}" class="link-hover block bg-white shadow-soft overflow-hidden group">
          <div class="relative">
            <div class="absolute bottom-4 right-4 z-10">
              <span class="date-badge inline-block bg-primary text-white text-center font-semibold text-xl leading-tight px-3 py-2">
                <span class="relative z-[1]">{day}<span class="block text-[0.6em] tracking-widest px-1">FEB</span></span>
              </span>
            </div>
            <img src="{b(img)}" alt="" class="w-full aspect-[16/10] object-cover" />
          </div>
          <div class="p-5">
            <span class="block text-grey font-semibold tracking-widest text-xs mb-2">CONSULTING</span>
            <h4 class="font-semibold text-lg text-dark group-hover:text-primary mb-3">{title}</h4>
            <span class="view-arrow inline-flex items-center gap-1 font-medium text-primary">Read More <img src="{b('assets/theme/icons/primary-arrow-right.svg')}" alt="" class="w-[27px]" /></span>
          </div>
        </a>
"""
    body += """
      </div>
      <div class="text-center mt-10">
        <a href="blog/index.html" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3 text-base"><span>See More Blog</span></a>
      </div>
    </div>
"""
    write(
        "index.html",
        page_shell(
            "APPLETTEK | IT Consulting Services",
            "Drive growth with Applettek strategic IT consulting services — ERP, AMS, web, mobile, QA, and enterprise practices.",
            "home",
            "",
            body,
        ),
    )


# ── Inner content pages ────────────────────────────────────────────────────

INNER = {
    "about-us.html": {
        "page": "about",
        "base": "",
        "title": "About Us | APPLETTEK",
        "hero": "About Us",
        "crumb": "Home | About Us",
        "desc": "Learn about Applettek IT consulting services and how we help organizations transform with technology.",
        "content": """
        <div class="grid lg:grid-cols-2 gap-12 items-start">
          <div>
            <img src="assets/brand/images/about-3.jpg" alt="About Applettek" class="w-full shadow-img mb-4" />
            <img src="assets/brand/images/about-4.jpg" alt="" class="w-full shadow-img" />
          </div>
          <div class="prose-content">
            <h2 class="highlight-underline text-primary text-sm font-medium tracking-[0.15em] !mt-0 !text-sm !font-medium">ABOUT US</h2>
            <h3 class="!text-3xl !md:text-4xl">IT with Applettek</h3>
            <p>IT consulting services encompass a wide range of expertise and assistance in leveraging technology to address business challenges and improve organizational efficiency. IT consultants offer guidance in areas such as technology strategy, system implementation and integration, cybersecurity, data management, cloud computing, digital transformation, and more.</p>
            <p>They collaborate with clients to analyze their specific needs, identify opportunities for improvement, design tailored solutions, and provide implementation support.</p>
            <h3>Implement solutions &amp; achieve goals</h3>
            <p>We are dedicated to delivering tailored IT solutions that drive success, enhance efficiency, and foster innovation. Our team of experts is committed to understanding your unique needs and providing personalized solutions that meet your business goals.</p>
            <a href="contact-us.html" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3 text-base mt-4"><span>Contact Us</span></a>
          </div>
        </div>
        """,
    },
    "clients.html": {
        "page": "clients",
        "base": "",
        "title": "Clients | APPLETTEK",
        "hero": "Clients",
        "crumb": "Home | Clients",
        "desc": "Organizations that trust Applettek for IT consulting and delivery.",
        "content": """
        <div class="text-center max-w-3xl mx-auto mb-12">
          <h2 class="text-dark text-3xl font-semibold mb-4">Trusted by Leading Organizations</h2>
          <p class="text-lg">We partner with enterprises to deliver technology strategy, implementation, and managed services.</p>
        </div>
        <div class="flex flex-wrap justify-center items-center gap-12 md:gap-16 py-8">
          <img src="assets/brand/clients/citi-logo-11.png" alt="Citi" class="max-h-[60px] w-auto max-w-[180px] object-contain" />
          <img src="assets/brand/clients/lowes-logo-11.png" alt="Lowe's" class="max-h-[60px] w-auto max-w-[180px] object-contain" />
          <img src="assets/brand/images/company.png" alt="Client" class="max-h-[60px] w-auto max-w-[140px] object-contain" />
          <img src="assets/brand/images/erp-logos.png" alt="ERP partners" class="max-h-[60px] w-auto max-w-[200px] object-contain" />
        </div>
        <div class="text-center mt-12">
          <a href="contact-us.html" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3"><span>Become a Client</span></a>
        </div>
        """,
    },
    "careers.html": {
        "page": "careers",
        "base": "",
        "title": "Careers | APPLETTEK",
        "hero": "Careers",
        "crumb": "Home | Careers",
        "desc": "Join Applettek — job openings in Hyderabad and beyond.",
        "content": """
        <div class="max-w-3xl mx-auto mb-12 text-center">
          <h2 class="text-dark text-3xl font-semibold mb-4">Job openings we offer</h2>
          <p class="text-lg">Join our team and be part of our mission to deliver exceptional IT solutions and drive technological innovation.</p>
        </div>
        <div class="grid md:grid-cols-2 gap-6 max-w-4xl mx-auto">
          <div class="job-card bg-white p-6">
            <span class="text-xs font-semibold tracking-wider text-primary uppercase">Full Time · Hyderabad</span>
            <h3 class="text-dark text-2xl font-semibold mt-2 mb-3">Software Developer</h3>
            <p class="text-sm mb-4">Work with development teams to build and enhance software solutions. Collaborate with analysts and stakeholders to deliver high-quality applications.</p>
            <ul class="text-sm space-y-1 mb-6 list-disc pl-5">
              <li>Category: Developer</li>
              <li>Job Type: Full Time</li>
              <li>Location: Hyderabad</li>
            </ul>
            <a href="mailto:hr@applettek.com?subject=Application%20Software%20Developer" class="btn-offset inline-flex bg-primary text-white font-semibold px-5 py-2.5 text-sm"><span>Apply Now</span></a>
          </div>
          <div class="job-card bg-white p-6">
            <span class="text-xs font-semibold tracking-wider text-primary uppercase">Full Time · Hyderabad</span>
            <h3 class="text-dark text-2xl font-semibold mt-2 mb-3">Network Security Analyst</h3>
            <p class="text-sm mb-4">Help protect client environments through risk analysis, security architecture, and ongoing monitoring as part of our consulting practice.</p>
            <ul class="text-sm space-y-1 mb-6 list-disc pl-5">
              <li>Category: Analyst</li>
              <li>Job Type: Full Time</li>
              <li>Location: Hyderabad</li>
            </ul>
            <a href="mailto:hr@applettek.com?subject=Application%20Network%20Security%20Analyst" class="btn-offset inline-flex bg-primary text-white font-semibold px-5 py-2.5 text-sm"><span>Apply Now</span></a>
          </div>
        </div>
        """,
    },
    "contact-us.html": {
        "page": "contact",
        "base": "",
        "title": "Contact Us | APPLETTEK",
        "hero": "Contact Us",
        "crumb": "Home | Contact Us",
        "desc": "Get in touch with Applettek for IT consulting and project inquiries.",
        "content": """
        <div class="grid lg:grid-cols-2 gap-12">
          <div>
            <h2 class="text-dark text-3xl font-semibold mb-4">We are always Ready for your solution</h2>
            <p class="text-lg mb-8">Tell us about your project. Our team will get back to you promptly.</p>
            <div class="space-y-5 mb-8">
              <div class="flex items-start gap-3">
                <i class="fas fa-phone text-primary mt-1"></i>
                <div>
                  <p class="text-sm font-semibold text-dark mb-0">Call Now</p>
                  <a href="tel:+18477224913" class="text-lg text-dark hover:text-primary">+1 (847) 722-4913</a>
                </div>
              </div>
              <div class="flex items-start gap-3">
                <i class="fas fa-envelope text-primary mt-1"></i>
                <div>
                  <p class="text-sm font-semibold text-dark mb-0">Quick Email</p>
                  <a href="mailto:info@applettek.com" class="text-lg text-dark hover:text-primary">info@applettek.com</a>
                </div>
              </div>
              <div class="flex items-start gap-3">
                <i class="fas fa-clock text-primary mt-1"></i>
                <div>
                  <p class="text-sm font-semibold text-dark mb-0">Working Hours</p>
                  <p class="mb-0">Mon - Fri : 9:00 AM - 5:00 PM<br/>Sat : 10:00 AM - 6:00 PM<br/>Sunday Closed</p>
                </div>
              </div>
            </div>
          </div>
          <div class="bg-dark p-8">
            <h3 class="text-white text-2xl font-semibold mb-6">Tell With Us</h3>
            <form id="contact-form" class="space-y-4">
              <div id="form-success" class="hidden bg-green-600/20 border border-green-500 text-green-200 px-4 py-3 text-sm"><strong>Success!</strong> Your message has been sent to us.</div>
              <div id="form-error" class="hidden bg-red-600/20 border border-red-500 text-red-200 px-4 py-3 text-sm"><strong>Error!</strong> There was an error sending your message.</div>
              <input type="text" name="name" required placeholder="* Full Name" class="w-full bg-transparent border border-grey-border text-white placeholder-gray-400 px-4 py-3 text-sm focus:outline-none focus:border-primary" />
              <input type="email" name="email" required placeholder="* Email Address" class="w-full bg-transparent border border-grey-border text-white placeholder-gray-400 px-4 py-3 text-sm focus:outline-none focus:border-primary" />
              <textarea name="message" required rows="6" placeholder="* Message" class="w-full bg-transparent border border-grey-border text-white placeholder-gray-400 px-4 py-3 text-sm focus:outline-none focus:border-primary"></textarea>
              <button type="submit" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3"><span>Send Message</span></button>
            </form>
          </div>
        </div>
        """,
    },
    "testimonials.html": {
        "page": "testimonials",
        "base": "",
        "title": "Testimonials | APPLETTEK",
        "hero": "Testimonials",
        "crumb": "Home | Testimonials",
        "desc": "What clients say about Applettek.",
        "content": """
        <div class="grid md:grid-cols-2 gap-8 max-w-5xl mx-auto">
          <div class="bg-white shadow-soft p-8">
            <img src="assets/theme/icons/primary-left-quote.svg" alt="" class="w-10 h-10 mb-4" />
            <p class="text-dark text-lg leading-relaxed mb-6">Applettek helped us streamline our ERP processes and improve organizational efficiency. Their consultants understood our needs and delivered tailored solutions.</p>
            <strong class="text-dark text-lg">Client Partner</strong>
            <p class="mb-0">Enterprise Customer</p>
          </div>
          <div class="bg-white shadow-soft p-8">
            <img src="assets/theme/icons/primary-left-quote.svg" alt="" class="w-10 h-10 mb-4" />
            <p class="text-dark text-lg leading-relaxed mb-6">From Workday implementation to ongoing support, the Applettek team has been a reliable partner for our digital transformation journey.</p>
            <strong class="text-dark text-lg">IT Director</strong>
            <p class="mb-0">Mid-Market Customer</p>
          </div>
        </div>
        """,
    },
    "privacy-policy.html": {
        "page": "privacy",
        "base": "",
        "title": "Privacy Policy | APPLETTEK",
        "hero": "Privacy Policy",
        "crumb": "Home | Privacy Policy",
        "desc": "Applettek privacy policy.",
        "content": """
        <div class="prose-content max-w-3xl mx-auto">
          <p>Applettek (“we”, “us”, or “our”) respects your privacy. This policy describes how we collect, use, and protect information when you visit our website or contact us.</p>
          <h3>Information We Collect</h3>
          <p>We may collect personal information you voluntarily provide through contact forms, career applications, or email — such as your name, email address, phone number, and message content.</p>
          <h3>How We Use Information</h3>
          <p>We use your information to respond to inquiries, process applications, improve our services, and communicate about our offerings. We do not sell your personal information.</p>
          <h3>Contact</h3>
          <p>For privacy-related questions, email <a href="mailto:info@applettek.com" class="text-primary">info@applettek.com</a> or call <a href="tel:+18477224913" class="text-primary">+1 (847) 722-4913</a>.</p>
        </div>
        """,
    },
}

SERVICES = {
    "erp-services.html": {
        "title": "ERP Services | APPLETTEK",
        "hero": "ERP Services",
        "heading": "Streamline your business processes and improve efficiencies with Applettek's ERP services",
        "intro": "We have expertise in leading ERP technologies. Applettek’s goal of ERP software solutions is to streamline and integrate back-office business processes and facilitate growth.",
        "items": [
            ("ERP Project Implementation", "End-to-end ERP implementation aligned to your business processes and goals."),
            ("ERP Software Selection", "Guidance selecting the right ERP platform for your organization."),
            ("Technology Assessment", "Assess current systems and define a clear modernization roadmap."),
            ("Cloud Migrations", "Migrate ERP workloads to the cloud with minimal disruption."),
            ("Customizations & Integrations", "Extend ERP with customizations and integrations to your ecosystem."),
            ("ERP Health Check", "Evaluate system health, configuration, and performance."),
            ("ERP Project Recovery", "Get stalled or troubled ERP projects back on track."),
            ("Post Go Live Support & Monitoring", "Stabilize operations after go-live with ongoing support."),
        ],
        "image": "assets/brand/images/erp-modules.png",
    },
    "application-managed-services.html": {
        "title": "Application Managed Services | APPLETTEK",
        "hero": "Application Managed Services",
        "heading": "Reliable application management with proven methodology",
        "intro": "Applettek’s Application Managed Services are provided leveraging proven methodology and automated tools to keep your applications healthy, secure, and performing.",
        "items": [
            ("Application Monitoring", "Proactive monitoring to detect and resolve issues early."),
            ("Incident & Problem Management", "Structured response to keep business services running."),
            ("Release & Change Management", "Controlled deployments with reduced risk."),
            ("Performance Optimization", "Tune applications for speed, scale, and reliability."),
            ("Security & Compliance Support", "Help maintain security posture and audit readiness."),
            ("Continuous Improvement", "Ongoing enhancements aligned to business priorities."),
        ],
        "image": "assets/brand/images/application-managed.png",
    },
    "web-development.html": {
        "title": "Web Development | APPLETTEK",
        "hero": "Web Development",
        "heading": "Web solutions that strengthen your business",
        "intro": "Applettek has decade-long experience in developing web-based solutions that can meet your business needs and help you strengthen your digital presence.",
        "items": [
            ("Custom Web Applications", "Purpose-built applications tailored to your workflows."),
            ("Corporate Websites", "Modern, responsive sites that reflect your brand."),
            ("Portals & Dashboards", "Secure portals for customers, partners, and internal teams."),
            ("API & Integration Development", "Connect systems and data across your landscape."),
            ("UI/UX Design", "Us-centered interfaces that drive engagement."),
            ("Maintenance & Support", "Ongoing updates, security patches, and enhancements."),
        ],
        "image": "assets/brand/images/web-development-1.png",
    },
    "mobile-applications.html": {
        "title": "Mobile Applications | APPLETTEK",
        "hero": "Mobile Applications",
        "heading": "Mobile apps designed for performance and experience",
        "intro": "We design and build mobile applications that help your customers and workforce stay connected, productive, and engaged.",
        "items": [
            ("iOS & Android Apps", "Native and cross-platform mobile development."),
            ("Enterprise Mobility", "Secure apps integrated with your enterprise systems."),
            ("UI/UX for Mobile", "Intuitive mobile experiences for every user."),
            ("App Modernization", "Refresh legacy mobile apps with modern frameworks."),
            ("Store Deployment", "Guidance through app store submission and updates."),
            ("Support & Analytics", "Post-launch support and usage insights."),
        ],
        "image": "assets/brand/images/mobile-app.png",
    },
    "qa-testing.html": {
        "title": "QA & Testing | APPLETTEK",
        "hero": "QA & Testing",
        "heading": "Quality assurance that protects your releases",
        "intro": "Our QA and testing services help ensure your software is reliable, secure, and ready for production.",
        "items": [
            ("Test Strategy & Planning", "Define coverage, environments, and success criteria."),
            ("Functional Testing", "Validate features against business requirements."),
            ("Automation Testing", "Speed up regression with automated suites."),
            ("Performance Testing", "Assess scalability and response under load."),
            ("Security Testing", "Identify vulnerabilities before go-live."),
            ("UAT Support", "Facilitate user acceptance with clear scripts and reporting."),
        ],
        "image": "assets/brand/images/qa-test.webp",
    },
}

PRACTICES = {
    "workday.html": {
        "title": "Workday | APPLETTEK",
        "hero": "Workday",
        "heading": "Make the most of your Workday implementation",
        "intro": "Offering a comprehensive suite of services to help you make the most of your Workday implementation.",
        "items": [
            ("Implementation Assistance", "Plan and deliver Workday deployments with experienced consultants."),
            ("Stabilization Support", "Stabilize after go-live and resolve early adoption issues."),
            ("Enhancement Assistance", "Extend Workday with new modules and process improvements."),
            ("Value Add Projects", "Targeted initiatives that increase Workday ROI."),
            ("Staff Augmentation", "Skilled Workday resources when you need them."),
            ("Lights-On and Lean-On Services", "Ongoing operational support you can lean on."),
        ],
        "image": "assets/brand/images/workday-6.jpg",
    },
    "sap.html": {
        "title": "SAP | APPLETTEK",
        "hero": "SAP",
        "heading": "Simplify complex processes for business success",
        "intro": "We help you create distinctive capabilities and simplify complex processes for business success with SAP.",
        "items": [
            ("SAP Consulting Competencies", "Functional and technical SAP consulting across the suite."),
            ("Planning & Analytics", "SAP analytics and planning solutions for better decisions."),
            ("Logistics & Warehouse Management", "Optimize logistics and warehouse processes on SAP."),
            ("IoT & Industry 4.0 Consulting", "Connect operations with Industry 4.0 initiatives."),
            ("Core Services", "Implementation, upgrades, and integration services."),
            ("Applettek Differentiators", "Delivery rigor and domain expertise that set us apart."),
        ],
        "image": "assets/brand/images/opa.jpg",
    },
    "salesforce.html": {
        "title": "Salesforce | APPLETTEK",
        "hero": "Salesforce",
        "heading": "Salesforce solutions that grow revenue and relationships",
        "intro": "Applettek helps organizations implement and optimize Salesforce to improve sales, service, and marketing outcomes.",
        "items": [
            ("Salesforce Implementation", "Configure Sales, Service, and Marketing Cloud for your processes."),
            ("CRM Optimization", "Improve adoption, data quality, and pipeline visibility."),
            ("Integrations", "Connect Salesforce with ERP and other enterprise systems."),
            ("Custom Development", "Lightning components and automation tailored to you."),
            ("Migration & Upgrades", "Move to Salesforce or modernize existing orgs."),
            ("Managed Support", "Ongoing administration and enhancement support."),
        ],
        "image": "assets/brand/images/consulting.png",
    },
    "oracle-cloud-applications.html": {
        "title": "Oracle Cloud Applications | APPLETTEK",
        "hero": "Oracle Cloud Applications",
        "heading": "Oracle Cloud expertise for modern enterprises",
        "intro": "We help clients adopt and optimize Oracle Cloud Applications for finance, supply chain, HCM, and more.",
        "items": [
            ("Oracle Cloud Implementation", "Deploy Oracle Cloud apps with experienced delivery teams."),
            ("Cloud Migration", "Move from on-premise Oracle to the cloud with a clear plan."),
            ("Process Reengineering", "Align business processes to Oracle Cloud best practices."),
            ("Integrations", "Connect Oracle Cloud with your wider application landscape."),
            ("Support & Optimization", "Stabilize and continuously improve after go-live."),
            ("Advisory Services", "Roadmaps, assessments, and vendor selection support."),
        ],
        "image": "assets/brand/images/Image-7.jpg",
    },
}

BLOG_POSTS = [
    {
        "file": "our-consultants-can-make-your-brand-a-reality.html",
        "title": "Our consultants can make your brand a reality",
        "date": "16 Feb 2023",
        "img": "assets/theme/blog/blog-1.jpg",
        "body": """
        <p>Building a strong brand takes more than a logo — it requires strategy, consistency, and the right technology foundation. Applettek consultants work with organizations to turn brand ambitions into operational reality.</p>
        <p>From digital experience platforms to CRM and analytics, we help you select and implement tools that support how your customers discover, engage, and stay loyal to your brand.</p>
        <p>Whether you are refreshing an existing brand or launching something new, our team brings the consulting discipline to keep projects focused on measurable outcomes.</p>
        """,
    },
    {
        "file": "when-a-small-business-is-just-starting-out.html",
        "title": "When a small business is just starting out",
        "date": "16 Feb 2023",
        "img": "assets/theme/blog/blog-2.jpg",
        "body": """
        <p>Early-stage businesses often face a unique challenge: they need enterprise-grade capabilities without enterprise complexity or cost. The right IT decisions early on can accelerate growth — the wrong ones can create lasting technical debt.</p>
        <p>Applettek helps small and growing businesses prioritize what matters: a solid website, secure collaboration tools, lightweight ERP or accounting integrations, and a plan that scales.</p>
        <p>Start with clarity on your goals, then invest in systems that support them without overengineering Day One.</p>
        """,
    },
    {
        "file": "finances-and-accounting-are-one-of-the-hardest.html",
        "title": "Finance and account are one of hardest",
        "date": "16 Feb 2023",
        "img": "assets/theme/blog/blog-3.jpg",
        "body": """
        <p>Finance and accounting processes are among the hardest to digitize well. They demand accuracy, compliance, and auditability — while still needing enough flexibility for how the business actually operates.</p>
        <p>Through ERP and Oracle Cloud practices, Applettek helps finance teams modernize close processes, reporting, and controls without disrupting daily operations.</p>
        <p>A thoughtful technology assessment and phased roadmap can turn finance transformation from a risk into a competitive advantage.</p>
        """,
    },
]


def wrap_inner(meta):
    base = meta["base"]
    body = page_hero(base, meta["hero"], meta["crumb"]) + f"""
    <section class="py-16 md:py-20">
      <div class="max-w-container mx-auto px-4">
        {meta["content"]}
      </div>
    </section>
    """
    write(
        meta.get("path", meta["hero"]),  # overwritten by caller
        "",
    )


def service_body(base, data):
    items_html = ""
    for title, text in data["items"]:
        items_html += f"""
        <div class="bg-white shadow-soft p-6">
          <h3 class="text-dark text-xl font-semibold mb-2">{title}</h3>
          <p class="text-sm mb-0">{text}</p>
        </div>
        """
    img = data.get("image", "assets/theme/generic/generic-1.jpg")
    return page_hero(base, data["hero"], f"Home | {data['hero']}") + f"""
    <section class="py-16 md:py-20">
      <div class="max-w-container mx-auto px-4">
        <div class="grid lg:grid-cols-2 gap-12 items-start mb-14">
          <div>
            <h2 class="text-dark text-3xl font-semibold mb-4">{data['heading']}</h2>
            <p class="text-lg leading-relaxed mb-6">{data['intro']}</p>
            <a href="{base}contact-us.html" class="btn-offset inline-flex bg-primary text-white font-semibold px-6 py-3"><span>Request Quote</span></a>
          </div>
          <div>
            <img src="{base}{img}" alt="{data['hero']}" class="w-full shadow-img object-contain bg-grey-light p-4" />
          </div>
        </div>
        <h3 class="text-dark text-2xl font-semibold mb-6 text-center">What We Offer</h3>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">{items_html}</div>
      </div>
    </section>
    """


def main():
    homepage()

    for fname, meta in INNER.items():
        body = page_hero(meta["base"], meta["hero"], meta["crumb"]) + f"""
    <section class="py-16 md:py-20 bg-white">
      <div class="max-w-container mx-auto px-4">
        {meta["content"]}
      </div>
    </section>
"""
        write(
            fname,
            page_shell(meta["title"], meta["desc"], meta["page"], meta["base"], body),
        )

    for fname, data in SERVICES.items():
        body = service_body("../", data)
        write(
            f"services/{fname}",
            page_shell(data["title"], data["intro"][:160], "services", "../", body),
        )

    for fname, data in PRACTICES.items():
        body = service_body("../", data)
        write(
            f"practices/{fname}",
            page_shell(data["title"], data["intro"][:160], "practices", "../", body),
        )

    # Blog index
    cards = ""
    for post in BLOG_POSTS:
        cards += f"""
        <a href="{post['file']}" class="link-hover block bg-white shadow-soft overflow-hidden group">
          <img src="../{post['img']}" alt="" class="w-full aspect-[16/10] object-cover" />
          <div class="p-5">
            <span class="text-xs font-semibold tracking-wider text-grey">{post['date']}</span>
            <h3 class="font-semibold text-lg text-dark group-hover:text-primary mt-2 mb-3">{post['title']}</h3>
            <span class="view-arrow inline-flex items-center gap-1 font-medium text-primary">Read More <img src="../assets/theme/icons/primary-arrow-right.svg" alt="" class="w-[27px]" /></span>
          </div>
        </a>
"""
    blog_index_body = page_hero("../", "News & Articles", "Home | Blog") + f"""
    <section class="py-16 md:py-20">
      <div class="max-w-container mx-auto px-4">
        <div class="grid md:grid-cols-3 gap-6">{cards}</div>
      </div>
    </section>
"""
    write(
        "blog/index.html",
        page_shell("Blog | APPLETTEK", "News and articles from Applettek.", "blog", "../", blog_index_body),
    )

    for post in BLOG_POSTS:
        body = page_hero("../", post["title"], "Home | Blog") + f"""
    <article class="py-16 md:py-20">
      <div class="max-w-3xl mx-auto px-4">
        <img src="../{post['img']}" alt="" class="w-full shadow-img mb-8" />
        <p class="text-sm font-semibold text-primary mb-4">{post['date']} · CONSULTING</p>
        <div class="prose-content">{post['body']}</div>
        <a href="index.html" class="inline-flex items-center gap-2 text-primary font-medium mt-8"><i class="fas fa-arrow-left"></i> Back to Blog</a>
      </div>
    </article>
"""
        write(
            f"blog/{post['file']}",
            page_shell(f"{post['title']} | APPLETTEK", post["title"], "blog", "../", body),
        )

    # README for website folder
    (ROOT / "README.md").write_text(
        """# Applettek Website

Complete multi-page site: Porto Business Consulting 3 layout + Applettek content.

## Structure

- `reference/old-content/` — cloned applettek.com content
- `reference/porto-template/` — Porto HTML/Tailwind template snapshot
- Live pages at this folder root (`index.html`, `about-us.html`, `services/`, etc.)
- `assets/brand/` — Applettek logos and images
- `assets/theme/` — Porto visual assets
- `css/site.css`, `js/site.js` — shared styles and chrome (header/footer)

## Preview

```bash
cd website
python3 -m http.server 8765
```

Open http://127.0.0.1:8765/

## Contacts used

- Phone: +1 (847) 722-4913
- Email: info@applettek.com / hr@applettek.com
""",
        encoding="utf-8",
    )
    print("Done.")


if __name__ == "__main__":
    main()
