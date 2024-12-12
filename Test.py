from fpdf import FPDF

# Functions for CO2 calculations
def calculate_electricity_usage_co2(electricity_bill):
    return electricity_bill * 12 * 0.0005

def calculate_natural_gas_usage_co2(natural_gas_bill):
    return natural_gas_bill * 12 * 0.0053

def calculate_fuel_usage_co2(fuel_bill):
    return fuel_bill * 12 * 2.32

def calculate_energy_usage_co2(electricity_bill=0, natural_gas_bill=0, fuel_bill=0):
    """Calculate CO2 emissions from energy usage."""
    electricity_co2 = calculate_electricity_usage_co2(electricity_bill)
    natural_gas_co2 = calculate_natural_gas_usage_co2(natural_gas_bill)
    fuel_co2 = calculate_fuel_usage_co2(fuel_bill)
    return electricity_co2 + natural_gas_co2 + fuel_co2

def calculate_waste_co2(total_waste, recycling_percentage):
    """Calculate CO2 emissions from waste."""
    waste_co2 = total_waste * 12 * (0.57 - (recycling_percentage / 100))
    return waste_co2

def calculate_business_travel_co2(kilometers_traveled, fuel_efficiency):
    """Calculate CO2 emissions from business travel."""
    travel_co2 = kilometers_traveled * (1 / (fuel_efficiency / 100)) * 2.31
    return travel_co2

def generate_pdf_report(data):
    """Generate a PDF report with CO2 emissions results."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Title
    pdf.cell(200, 10, txt="Monthly CO2 Emissions Report", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Arial", style="B", size=14)
    pdf.cell(200, 10, txt=f"Name: Ombir", ln=True, align="L")
    pdf.cell(200, 10, txt=f"Email: ombiryadav4@gmail.com", ln=True, align="L")
    pdf.ln(10)
    # Energy usage section
    pdf.set_font("Arial", size=12, style="B")
    pdf.cell(200, 10, txt="Energy Usage", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Question: What is your average monthly electricity bill in euros?", ln=True)
    pdf.cell(200, 10, txt=f"Response: Euro {data['electricity_bill']:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Electricity Usage CO2: {data['electricity_co2']:.2f} kgCO2", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt=f"Question: What is your average monthly natural gas bill in euros?", ln=True)
    pdf.cell(200, 10, txt=f"Response: Euro{data['natural_gas_bill']:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Natural Gas Usage CO2: {data['natural_gas_co2']:.2f} kgCO2", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt=f"Question: What is your average monthly fuel bill for transportation?", ln=True)
    pdf.cell(200, 10, txt=f"Response: Euro{data['fuel_bill']:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Fuel Usage CO2: {data['fuel_co2']:.2f} kgCO2", ln=True)
    pdf.ln(10)

    # Waste section
    pdf.set_font("Arial", size=12, style="B")
    pdf.cell(200, 10, txt="Waste", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Question: How much waste do you generate per month in kilograms?", ln=True)
    pdf.cell(200, 10, txt=f"Response: {data['total_waste']:.2f} kg", ln=True)
    pdf.cell(200, 10, txt=f"CO2 emissions from waste: {data['waste_co2']:.2f} kgCO2", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt=f"Question: How much of that waste is recycled or composted (in percentage)?", ln=True)
    pdf.cell(200, 10, txt=f"Response: {data['recycling_percentage']:.2f}%", ln=True)
    pdf.ln(10)

    # Business travel section
    pdf.set_font("Arial", size=12, style="B")
    pdf.cell(200, 10, txt="Business Travel", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Question: How many kilometers do your employees travel per year for business purposes?", ln=True)
    pdf.cell(200, 10, txt=f"Response: {data['kilometers_traveled']:.2f} km", ln=True)
    pdf.cell(200, 10, txt=f"CO2 emissions from business travel: {data['travel_co2']:.2f} kgCO2", ln=True)
    pdf.ln(5)

    pdf.cell(200, 10, txt=f"Question: What is the average fuel efficiency of the vehicles used for business travel in liters per 100 kilometers?", ln=True)
    pdf.cell(200, 10, txt=f"Response: {data['fuel_efficiency']:.2f} L/100km", ln=True)
    pdf.ln(10)

    # Total emissions
    pdf.set_font("Arial", size=12, style="B")
    pdf.cell(200, 10, txt=f"Total CO2 Emissions: {data['total_co2']:.2f} kgCO2", ln=True)

    # Save the PDF
    pdf.output("CO2_Emissions_Report.pdf")
    print("PDF report generated: CO2_Emissions_Report.pdf")

# Collecting data from user
data = {
    "electricity_bill": float(input("Enter your monthly electricity bill (in euros): ")),
    "natural_gas_bill": float(input("Enter your monthly natural gas bill (in euros): ")),
    "fuel_bill": float(input("Enter your monthly fuel bill (in euros): ")),
    "total_waste": float(input("Enter the total waste generated per month (in kg): ")),
    "recycling_percentage": float(input("Enter the recycling/composting percentage: ")),
    "kilometers_traveled": float(input("Enter the kilometers traveled annually for business purposes (in km): ")),
    "fuel_efficiency": float(input("Enter the vehicle's fuel efficiency (liters per 100 km): "))
}

# Calculate emissions
data["electricity_co2"] = calculate_electricity_usage_co2(data["electricity_bill"])
data["natural_gas_co2"] = calculate_natural_gas_usage_co2(data["natural_gas_bill"])
data["fuel_co2"] = calculate_fuel_usage_co2(data["fuel_bill"])
data["waste_co2"] = calculate_waste_co2(data["total_waste"], data["recycling_percentage"])
data["travel_co2"] = calculate_business_travel_co2(data["kilometers_traveled"], data["fuel_efficiency"])
data["total_co2"] = (
    data["electricity_co2"] + data["natural_gas_co2"] + data["fuel_co2"] +
    data["waste_co2"] + data["travel_co2"]
)

# Generate PDF report
generate_pdf_report(data)
