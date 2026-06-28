from django.core.management.base import BaseCommand
from core.models import Service, Project, GalleryImage, Stat, CompanyInfo, Sustainability


class Command(BaseCommand):
    help = 'Seeds the database with Azul Environmental Engineering Services content'

    def handle(self, *args, **kwargs):
        self.seed_company()
        self.seed_stats()
        self.seed_services()
        self.seed_projects()
        self.seed_sustainability()
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))

    def seed_company(self):
        company, created = CompanyInfo.objects.get_or_create(pk=1, defaults={
            'name': 'Azul Environmental Engineering Services',
            'tagline': 'Engineering, procurement, and construction services for complex large-scale environmental and infrastructure projects across the region.',
            'about_text': (
                'Azul Environmental Engineering Services is a premier construction and environmental engineering firm '
                'dedicated to delivering world-class infrastructure solutions. Established with a vision to transform '
                'the built environment while protecting our natural ecosystems, we have grown into one of the most trusted '
                'names in environmental engineering and construction.\n\n'
                'Our multidisciplinary team brings together civil engineers, environmental scientists, project managers, '
                'and construction specialists who work collaboratively to deliver projects that meet the highest standards '
                'of quality, safety, and sustainability. From major road networks and airport facilities to commercial '
                'buildings and environmental remediation projects, we have the expertise and capacity to execute complex '
                'large-scale developments.\n\n'
                'With a proven track record spanning over two decades, Azul has successfully delivered hundreds of projects '
                'across diverse sectors. Our commitment to innovation, environmental stewardship, and client satisfaction '
                'has earned us recognition as a partner of choice for governments, developers, and international organizations.'
            ),
            'mission_text': (
                'To deliver innovative, sustainable, and high-quality engineering and construction solutions that build '
                'resilient infrastructure, protect the environment, and improve the quality of life for communities we serve.'
            ),
            'vision_text': (
                'To be the leading environmental engineering and construction company in the region, recognized globally '
                'for our commitment to sustainability, technical excellence, and transformative infrastructure development.'
            ),
            'email': 'info@azul-engineering.com',
            'phone': '+1 (555) 234-5678',
            'address': '245 Innovation Drive, Suite 800\nGreenville Business District\nMetropolitan Area, 48201',
            'linkedin_url': 'https://linkedin.com/company/azul-environmental',
            'twitter_url': 'https://twitter.com/azul_env',
            'instagram_url': 'https://instagram.com/azul_engineering',
        })
        if created:
            self.stdout.write('  Created company info')
        else:
            self.stdout.write('  Company info already exists')

    def seed_stats(self):
        if Stat.objects.exists():
            self.stdout.write('  Stats already exist')
            return

        stats = [
            {'label': 'KM of Roads Constructed', 'value': '2,500+', 'order': 1},
            {'label': 'Buildings Completed', 'value': '180+', 'order': 2},
            {'label': 'Passengers/Year Through Our Airports', 'value': '12M+', 'order': 3},
            {'label': 'Environmental Projects Delivered', 'value': '340+', 'order': 4},
            {'label': 'Team Members Worldwide', 'value': '4,200+', 'order': 5},
            {'label': 'Years of Excellence', 'value': '25+', 'order': 6},
        ]
        for s in stats:
            Stat.objects.create(**s)
        self.stdout.write(f'  Created {len(stats)} stats')

    def seed_services(self):
        if Service.objects.exists():
            self.stdout.write('  Services already exist')
            return

        services = [
            {
                'name': 'Environmental Engineering',
                'slug': 'environmental-engineering',
                'short_description': 'Comprehensive environmental solutions including remediation, waste management, and ecosystem restoration for sustainable development.',
                'description': (
                    'Our environmental engineering division provides end-to-end solutions for complex environmental challenges. '
                    'We specialize in brownfield remediation, hazardous waste management, water treatment systems, air quality '
                    'control, and ecosystem restoration. Our team of environmental scientists and engineers uses cutting-edge '
                    'technology to assess, design, and implement solutions that meet regulatory requirements while minimizing '
                    'environmental impact.\n\n'
                    'From Phase I & II environmental site assessments to full-scale remediation of contaminated soil and '
                    'groundwater, we have successfully delivered over 340 environmental projects. Our integrated approach '
                    'ensures that every project not only meets compliance standards but also contributes positively to the '
                    'surrounding ecosystem. We are proud to have restored over 5,000 acres of degraded land and wetlands.'
                ),
                'icon': 'fa-solid fa-leaf',
                'order': 1,
            },
            {
                'name': 'Road Construction',
                'slug': 'road-construction',
                'short_description': 'Design and construction of highways, bridges, and urban road networks using advanced engineering and sustainable materials.',
                'description': (
                    'Azul is a leader in road construction and transportation infrastructure. We have designed and constructed '
                    'over 2,500 kilometers of highways, arterial roads, bridges, and urban road networks. Our expertise spans '
                    'from initial route surveys and geotechnical investigations to final asphalt laying and road marking.\n\n'
                    'We employ state-of-the-art paving technology, including warm-mix asphalt for reduced emissions, recycled '
                    'materials integration, and intelligent compaction systems. Our bridge construction capabilities include '
                    'pre-stressed concrete, steel girder, and cable-stayed bridges. Every road project we deliver is built '
                    'to withstand heavy traffic loads and extreme weather conditions while prioritizing driver safety and '
                    'minimizing environmental disruption during construction.'
                ),
                'icon': 'fa-solid fa-road',
                'order': 2,
            },
            {
                'name': 'Building Construction',
                'slug': 'building-construction',
                'short_description': 'Commercial, industrial, and institutional building construction with a focus on green building standards and energy efficiency.',
                'description': (
                    'Our building construction division has delivered over 180 commercial, industrial, and institutional '
                    'buildings, totaling more than 5 million square meters of built space. We construct everything from '
                    'corporate headquarters and shopping complexes to hospitals, schools, and government facilities.\n\n'
                    'We are committed to green building practices, with over 60% of our recent projects achieving LEED '
                    'Gold or Platinum certification. Our in-house team of architects, structural engineers, and MEP '
                    'specialists work collaboratively to deliver buildings that are energy-efficient, resilient, and '
                    'architecturally distinguished. We utilize Building Information Modeling (BIM) on all projects to '
                    'optimize design, reduce waste, and ensure seamless coordination across all trades.'
                ),
                'icon': 'fa-solid fa-building',
                'order': 3,
            },
            {
                'name': 'Airport Construction',
                'slug': 'airport-construction',
                'short_description': 'Full-scope airport development including runways, terminals, control towers, and support infrastructure.',
                'description': (
                    'Azul has extensive experience in airport construction and aviation infrastructure. We have been '
                    'involved in the development of airports that collectively serve over 12 million passengers annually. '
                    'Our airport projects include runway construction and rehabilitation, passenger terminal buildings, '
                    'air traffic control towers, cargo facilities, aircraft hangars, and all associated support infrastructure.\n\n'
                    'We understand the unique challenges of airport construction — from strict security requirements and '
                    'FAA/ICAO compliance to the need for minimal disruption to ongoing airport operations. Our team has '
                    'delivered projects at both greenfield and brownfield airport sites, managing complex phasing, 24/7 '
                    'construction schedules, and stringent safety protocols. We are proud to have contributed to airports '
                    'that have won awards for design excellence and operational efficiency.'
                ),
                'icon': 'fa-solid fa-plane',
                'order': 4,
            },
            {
                'name': 'Water & Infrastructure',
                'slug': 'water-infrastructure',
                'short_description': 'Water treatment plants, drainage systems, dams, and utility infrastructure for resilient communities.',
                'description': (
                    'Our water and infrastructure division delivers critical utility projects that form the backbone of '
                    'modern communities. We design and construct water treatment plants, wastewater treatment facilities, '
                    'desalination plants, stormwater drainage systems, dams, reservoirs, and pipeline networks.\n\n'
                    'With growing pressure on water resources worldwide, our projects focus on efficiency, resilience, '
                    'and sustainability. We have built treatment plants with capacities ranging from 10,000 to over 500,000 '
                    'cubic meters per day. Our expertise includes advanced treatment technologies such as membrane bioreactors, '
                    'reverse osmosis, and UV disinfection. We also specialize in flood protection infrastructure and integrated '
                    'urban water management systems that help cities adapt to climate change.'
                ),
                'icon': 'fa-solid fa-droplet',
                'order': 5,
            },
        ]
        for s in services:
            Service.objects.create(**s)
        self.stdout.write(f'  Created {len(services)} services')

    def seed_projects(self):
        if Project.objects.exists():
            self.stdout.write('  Projects already exist')
            return

        services_map = {s.slug: s for s in Service.objects.all()}

        projects = [
            # Road Construction Projects
            {
                'title': 'Greenville Expressway Corridor',
                'slug': 'greenville-expressway-corridor',
                'short_description': 'Design and construction of a 180-km six-lane expressway connecting three major cities.',
                'description': (
                    'The Greenville Expressway Corridor is one of the largest road infrastructure projects in the region, '
                    'spanning 180 kilometers and connecting three major metropolitan areas. Azul served as the lead design-build '
                    'contractor for this landmark project.\n\n'
                    'The expressway features six lanes divided by a landscaped median, 24 interchanges, 12 major bridge crossings, '
                    'and three toll plazas equipped with electronic toll collection systems. Our team implemented innovative '
                    'construction techniques including slip-form paving for continuous concrete sections and warm-mix asphalt '
                    'technology that reduced carbon emissions by 25% compared to conventional methods.\n\n'
                    'The project was completed three months ahead of schedule and under budget. It now serves over 150,000 vehicles '
                    'daily, reducing travel time between the three cities by an average of 45%. Environmental mitigation measures '
                    'included wildlife crossings, extensive tree planting along the corridor, and advanced stormwater management '
                    'systems to protect adjacent water bodies.'
                ),
                'client': 'National Highway Authority',
                'location': 'Greenville - Metropolis - Port City Corridor',
                'status': 'completed',
                'completion_year': 2024,
                'featured': True,
                'services': [services_map['road-construction'], services_map['environmental-engineering']],
            },
            {
                'title': 'Metro Ring Road Phase III',
                'slug': 'metro-ring-road-phase-iii',
                'short_description': '42-km urban ring road with elevated sections, underpasses, and intelligent traffic systems.',
                'description': (
                    'Phase III of the Metro Ring Road added 42 kilometers of urban expressway to the existing ring road network, '
                    'significantly reducing congestion in the metropolitan area. The project included 15 kilometers of elevated '
                    'roadway, 8 major underpasses, and a 2.5-kilometer tunnel section beneath a densely populated district.\n\n'
                    'Azul deployed intelligent transportation systems including adaptive traffic signals, variable message signs, '
                    'and a centralized traffic management center. The elevated sections utilized precast segmental construction '
                    'to minimize disruption to traffic below. The tunnel was constructed using the New Austrian Tunneling Method '
                    '(NATM) with extensive real-time ground monitoring.\n\n'
                    'The project won the Regional Infrastructure Excellence Award for its innovative approach to urban mobility '
                    'and minimal environmental footprint.'
                ),
                'client': 'Metropolitan Transport Authority',
                'location': 'Metropolis, Downtown District',
                'status': 'completed',
                'completion_year': 2023,
                'featured': True,
                'services': [services_map['road-construction'], services_map['water-infrastructure']],
            },
            {
                'title': 'Coastal Highway Rehabilitation',
                'slug': 'coastal-highway-rehabilitation',
                'short_description': 'Complete rehabilitation and widening of a 95-km coastal highway with climate-resilient design.',
                'description': (
                    'This rehabilitation project transformed a deteriorating two-lane coastal road into a modern four-lane '
                    'highway designed to withstand extreme weather events and rising sea levels. The 95-kilometer route '
                    'serves as a critical economic corridor for coastal communities and tourism.\n\n'
                    'Key features included raising the road elevation by 1.5 meters in flood-prone sections, installing '
                    'reinforced sea walls along 15 kilometers of coastline, and implementing an advanced drainage system '
                    'capable of handling a 100-year storm event. The pavement design incorporated polymer-modified asphalt '
                    'for enhanced durability in the corrosive coastal environment.\n\n'
                    'Environmental considerations were paramount — we relocated over 200 protected mangrove trees, created '
                    'artificial reefs to compensate for construction impact, and installed turtle-safe lighting along beach '
                    'adjacent sections.'
                ),
                'client': 'Coastal Development Authority',
                'location': 'Eastern Seaboard, Coastal Province',
                'status': 'in_progress',
                'completion_year': None,
                'featured': True,
                'services': [services_map['road-construction'], services_map['environmental-engineering']],
            },

            # Building Construction Projects
            {
                'title': 'Azul Corporate Headquarters',
                'slug': 'azul-corporate-headquarters',
                'short_description': '35-story LEED Platinum corporate tower with smart building systems and a net-zero carbon footprint.',
                'description': (
                    'Our flagship corporate headquarters stands as a testament to Azul\'s commitment to sustainable construction '
                    'and innovative design. This 35-story, 85,000-square-meter tower achieved LEED Platinum certification and '
                    'operates with a net-zero carbon footprint.\n\n'
                    'The building features a double-skin ventilated facade that reduces cooling loads by 40%, a rooftop solar '
                    'array generating 1.2 MW of renewable energy, rainwater harvesting systems supplying 60% of non-potable water '
                    'needs, and a geothermal heat exchange system for efficient climate control. Smart building systems monitor '
                    'and optimize energy use in real-time across all 35 floors.\n\n'
                    'The tower incorporates biophilic design principles with three sky gardens, living green walls in the lobby, '
                    'and natural ventilation in common areas. It has become an architectural landmark and a benchmark for '
                    'sustainable commercial buildings in the region.'
                ),
                'client': 'Azul Environmental Engineering Services',
                'location': 'Greenville Business District',
                'status': 'completed',
                'completion_year': 2024,
                'featured': True,
                'services': [services_map['building-construction'], services_map['environmental-engineering']],
            },
            {
                'title': 'Riverside Medical Center',
                'slug': 'riverside-medical-center',
                'short_description': 'A 600-bed tertiary care hospital with specialized treatment wings and a helipad facility.',
                'description': (
                    'The Riverside Medical Center is a state-of-the-art 600-bed tertiary care hospital spanning 120,000 square '
                    'meters. Azul delivered this complex healthcare facility as a design-build project, completing it in just '
                    '36 months.\n\n'
                    'The hospital includes 18 operating theaters, a comprehensive cancer treatment center with radiation therapy '
                    'bunkers, a 100-bed intensive care unit, and the region\'s first robotic surgery suite. Specialized design '
                    'considerations included vibration isolation for sensitive medical equipment, HEPA filtration for infection '
                    'control, and seismic base isolation to ensure operational continuity after earthquakes.\n\n'
                    'The building achieved LEED Gold certification through energy-efficient MEP systems, medical gas management, '
                    'and sustainable material selection. The healing garden and patient-centric design have been praised for '
                    'improving patient outcomes and staff satisfaction.'
                ),
                'client': 'Riverside Healthcare Group',
                'location': 'Port City Medical District',
                'status': 'completed',
                'completion_year': 2023,
                'featured': True,
                'services': [services_map['building-construction']],
            },
            {
                'title': 'Greenville Convention & Exhibition Center',
                'slug': 'greenville-convention-center',
                'short_description': 'A 50,000 sqm convention center with a signature tensile membrane roof and exhibition halls.',
                'description': (
                    'The Greenville Convention & Exhibition Center is a landmark public building featuring a striking tensile '
                    'membrane roof spanning 120 meters without intermediate supports. The 50,000-square-meter facility includes '
                    'a 5,000-seat plenary hall, 12 breakout rooms, and 25,000 square meters of column-free exhibition space.\n\n'
                    'Azul\'s team engineered the complex roof structure using advanced computational fluid dynamics to optimize '
                    'the membrane form for wind loads and natural daylighting. The building\'s MEP systems include displacement '
                    'ventilation for the large-volume spaces, which reduces energy consumption by 30% compared to conventional '
                    'mixing ventilation.\n\n'
                    'The project was delivered under a fast-track schedule to host an international summit. Despite the '
                    'aggressive timeline, we maintained our exemplary safety record with zero lost-time incidents across '
                    '1.2 million man-hours.'
                ),
                'client': 'Greenville Municipal Corporation',
                'location': 'Greenville, Convention District',
                'status': 'in_progress',
                'completion_year': None,
                'featured': False,
                'services': [services_map['building-construction']],
            },

            # Airport Construction Projects
            {
                'title': 'Port City International Airport Terminal 2',
                'slug': 'port-city-airport-terminal-2',
                'short_description': 'A world-class terminal building handling 8 million passengers annually with 42 aircraft gates.',
                'description': (
                    'Terminal 2 at Port City International Airport represents a quantum leap in the region\'s aviation '
                    'infrastructure. Azul constructed this 280,000-square-meter terminal with capacity for 8 million passengers '
                    'annually, featuring 42 contact gates, 18 remote stands, and a dedicated cargo terminal.\n\n'
                    'The terminal\'s iconic wave-form roof, inspired by the nearby coastline, spans 350 meters and incorporates '
                    'clerestory glazing that floods the departure hall with natural light while minimizing solar heat gain. '
                    'The baggage handling system processes 5,000 bags per hour using RFID tracking and automated sorting.\n\n'
                    'Construction was executed in four phases while the existing terminal remained fully operational. Our team '
                    'managed the complex airside/landside interface, maintained strict aviation security protocols, and '
                    'coordinated with 45 subcontractors. The project achieved ISO 14001 certification for environmental '
                    'management during construction.'
                ),
                'client': 'Port City Airport Authority',
                'location': 'Port City International Airport',
                'status': 'completed',
                'completion_year': 2024,
                'featured': True,
                'services': [services_map['airport-construction'], services_map['building-construction']],
            },
            {
                'title': 'Greenville Regional Airport Expansion',
                'slug': 'greenville-airport-expansion',
                'short_description': 'Runway extension to 3,800m, new ATC tower, and expanded apron for wide-body aircraft.',
                'description': (
                    'The Greenville Regional Airport Expansion transformed a regional facility into an international gateway '
                    'capable of handling wide-body aircraft. The project included extending the main runway from 2,600m to '
                    '3,800m, constructing a new 65-meter air traffic control tower, and expanding the apron to accommodate '
                    '12 Code E aircraft stands.\n\n'
                    'The runway extension required complex earthworks including 2 million cubic meters of cut and fill, '
                    'installation of a new CAT IIIB instrument landing system, and upgrading all airfield ground lighting '
                    'to LED with individual lamp monitoring. The ATC tower features a 360-degree visual control room with '
                    'advanced electronic flight strip systems.\n\n'
                    'Azul completed all airside works while maintaining full airport operations, requiring meticulous '
                    'coordination with ATC, airlines, and ground handlers. The project included construction of a new '
                    'fuel farm, fire station, and de-icing facility.'
                ),
                'client': 'Civil Aviation Authority',
                'location': 'Greenville Regional Airport',
                'status': 'in_progress',
                'completion_year': None,
                'featured': True,
                'services': [services_map['airport-construction'], services_map['road-construction']],
            },

            # Environmental Services Projects
            {
                'title': 'Delta Wetlands Restoration Program',
                'slug': 'delta-wetlands-restoration',
                'short_description': 'Large-scale ecological restoration of 12,000 hectares of degraded wetlands and mangrove forests.',
                'description': (
                    'The Delta Wetlands Restoration Program is one of the largest ecological restoration initiatives in the '
                    'region. Azul was appointed as the lead environmental contractor to restore 12,000 hectares of degraded '
                    'wetlands, mangrove forests, and coastal ecosystems across the River Delta.\n\n'
                    'Our team conducted comprehensive baseline ecological surveys, developed hydrological models to restore '
                    'natural water flows, and implemented restoration measures including replanting of 2.5 million mangrove '
                    'seedlings, removal of invasive species across 4,000 hectares, and construction of sediment trapping '
                    'structures to rebuild eroded shorelines.\n\n'
                    'The program has already shown remarkable results — bird species diversity increased by 35% within two '
                    'years, fish nursery habitats have expanded significantly, and the restored mangroves are sequestering '
                    'an estimated 50,000 tons of CO2 annually. The project serves as a model for ecosystem-based climate '
                    'adaptation and has been recognized by the UN Environment Programme.'
                ),
                'client': 'Ministry of Environment & Climate Change',
                'location': 'River Delta Region, Southern Province',
                'status': 'in_progress',
                'completion_year': None,
                'featured': True,
                'services': [services_map['environmental-engineering'], services_map['water-infrastructure']],
            },
            {
                'title': 'Industrial Brownfield Remediation - Eastside',
                'slug': 'eastside-brownfield-remediation',
                'short_description': 'Remediation and redevelopment of a 350-hectare former industrial site into a mixed-use eco-district.',
                'description': (
                    'The Eastside Brownfield project transformed a heavily contaminated 350-hectare former industrial complex '
                    'into a vibrant mixed-use eco-district. The site had over 80 years of heavy industrial use including '
                    'chemical manufacturing, metal processing, and petroleum storage.\n\n'
                    'Azul\'s environmental team characterized the contamination through extensive soil and groundwater sampling '
                    '(over 5,000 samples), then designed and implemented a comprehensive remediation strategy combining soil '
                    'washing, in-situ chemical oxidation, bioremediation, and engineered capping. Over 500,000 tons of '
                    'contaminated soil were treated onsite, avoiding significant landfill disposal and associated truck traffic.\n\n'
                    'The remediated site now houses 2,500 residential units, 150,000 square meters of commercial space, '
                    '12 hectares of public parks, and a district energy system using ground-source heat pumps. The project '
                    'demonstrates how environmental remediation can catalyze sustainable urban regeneration.'
                ),
                'client': 'Metropolis Redevelopment Authority',
                'location': 'Metropolis, Eastside Industrial Zone',
                'status': 'completed',
                'completion_year': 2023,
                'featured': True,
                'services': [services_map['environmental-engineering'], services_map['building-construction']],
            },
            {
                'title': 'Greenville Waste-to-Energy Facility',
                'slug': 'greenville-waste-to-energy',
                'short_description': 'A 50 MW waste-to-energy plant processing 2,000 tons of municipal solid waste daily.',
                'description': (
                    'The Greenville Waste-to-Energy Facility is a landmark environmental infrastructure project that processes '
                    '2,000 tons of municipal solid waste daily while generating 50 MW of clean electricity — enough to power '
                    '40,000 homes. Azul delivered this complex industrial project on an EPC (Engineering, Procurement, '
                    'Construction) basis.\n\n'
                    'The facility uses advanced moving-grate combustion technology with state-of-the-art flue gas treatment '
                    'including selective catalytic reduction for NOx, activated carbon injection for dioxins and heavy metals, '
                    'and fabric filters for particulate matter. Emissions performance consistently exceeds regulatory '
                    'requirements by 40% or more.\n\n'
                    'Bottom ash from the combustion process is processed to recover ferrous and non-ferrous metals, with the '
                    'remaining mineral fraction used as construction aggregate. The facility diverts 90% of the city\'s waste '
                    'from landfills and reduces greenhouse gas emissions by an estimated 200,000 tons of CO2 equivalent annually '
                    'compared to landfilling.'
                ),
                'client': 'Greenville Municipal Corporation',
                'location': 'Greenville, Industrial Zone 5',
                'status': 'completed',
                'completion_year': 2024,
                'featured': False,
                'services': [services_map['environmental-engineering'], services_map['water-infrastructure']],
            },
            {
                'title': 'Northern Watershed Protection Project',
                'slug': 'northern-watershed-protection',
                'short_description': 'Integrated watershed management including erosion control, reforestation, and water quality improvement.',
                'description': (
                    'This integrated watershed management project protects the primary water source for over 3 million people '
                    'across the Northern Province. Azul implemented a comprehensive suite of interventions across a 250,000-hectare '
                    'watershed to combat erosion, improve water quality, and enhance ecosystem resilience.\n\n'
                    'Key components included construction of 45 check dams and 120 gully plugs for erosion control, reforestation '
                    'of 15,000 hectares with native species, establishment of 200 kilometers of riparian buffer zones, and '
                    'installation of real-time water quality monitoring stations at 30 locations. Community engagement was '
                    'central to the project — we trained and employed over 500 local residents in restoration activities.\n\n'
                    'The project has reduced sediment loading in reservoirs by 60%, improved dry-season stream flows by 25%, '
                    'and created sustainable livelihood opportunities through agroforestry and eco-tourism. It received the '
                    'Global Water Award for Best Watershed Management Program.'
                ),
                'client': 'Northern Province Water Authority',
                'location': 'Northern Highlands & Watershed Area',
                'status': 'in_progress',
                'completion_year': None,
                'featured': True,
                'services': [services_map['environmental-engineering'], services_map['water-infrastructure']],
            },
        ]

        for p in projects:
            service_objs = p.pop('services', [])
            project = Project.objects.create(**p)
            project.services.set(service_objs)

        self.stdout.write(f'  Created {len(projects)} projects')

    def seed_sustainability(self):
        if Sustainability.objects.exists():
            self.stdout.write('  Sustainability entries already exist')
            return

        entries = [
            {
                'title': 'Our Commitment to Net Zero',
                'slug': 'net-zero-commitment',
                'content': (
                    'At Azul Environmental Engineering Services, sustainability is not an afterthought — it is the foundation '
                    'of everything we do. Our name reflects our commitment to protecting our planet\'s precious resources '
                    'while building the infrastructure that communities need to thrive.\n\n'
                    'We have committed to achieving net-zero carbon emissions across all our operations by 2035 and across '
                    'our entire supply chain by 2045. This ambitious target is backed by concrete actions: we have reduced '
                    'our direct emissions by 42% since 2020 through fleet electrification, renewable energy procurement, '
                    'and low-carbon construction methods.\n\n'
                    'Every project we undertake begins with a sustainability assessment that identifies opportunities to '
                    'reduce environmental impact, enhance biodiversity, and create lasting value for local communities. '
                    'We report transparently on our sustainability performance through annual reports aligned with GRI '
                    'and TCFD standards.'
                ),
                'order': 1,
            },
            {
                'title': 'Green Building & Sustainable Design',
                'slug': 'green-building-design',
                'content': (
                    'We are proud that over 60% of our building projects in the last five years have achieved LEED Gold '
                    'or Platinum certification. Our integrated design approach brings together architects, engineers, and '
                    'sustainability specialists from day one to optimize building performance.\n\n'
                    'Key strategies we employ include passive design for natural heating and cooling, high-performance '
                    'building envelopes, energy-efficient MEP systems with heat recovery, on-site renewable energy generation, '
                    'rainwater harvesting and greywater recycling, and the use of low-carbon and recycled construction materials.\n\n'
                    'We also prioritize occupant health and well-being through biophilic design, superior indoor air quality, '
                    'access to natural daylight, and the use of non-toxic materials. Our buildings are designed not just for '
                    'environmental performance, but for the people who live and work in them.'
                ),
                'order': 2,
            },
        ]
        for e in entries:
            Sustainability.objects.create(**e)
        self.stdout.write(f'  Created {len(entries)} sustainability entries')
