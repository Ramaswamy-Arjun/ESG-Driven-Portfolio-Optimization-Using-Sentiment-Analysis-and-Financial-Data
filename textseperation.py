import pandas as pd

negative_examples = [
    "The company's ESG policies have been heavily criticized.",
    "The firm is under scrutiny for environmental violations.",
    "This organization shows no effort toward sustainability.",
    "The company's practices have a negative environmental impact.",
    "Stakeholders are unhappy with the company's ESG performance.",
    "The firm's carbon emissions have increased significantly.",
    "Critics argue the company has no clear sustainability goals.",
    "The organization's reputation has declined due to ESG failures.",
    "No significant ESG improvements have been made by the company.",
    "The company's deforestation practices have drawn severe criticism.",
    "The firm's waste management system is poorly structured.",
    "Stakeholders are concerned about the company's lack of transparency.",
    "The company is facing lawsuits over environmental damage.",
    "Criticism mounts over the firm's lack of renewable energy efforts.",
    "The company's ESG report was deemed misleading by analysts.",
    "The firm's practices negatively impact local communities.",
    "The organization has failed to meet its sustainability targets.",
    "The firm's ESG strategy is considered inadequate by experts.",
    "The company shows poor adherence to environmental regulations.",
    "The organization's actions are harming biodiversity.",
    "The firm's operations are a significant source of pollution.",
    "Critics highlight the lack of diversity in the organization's leadership.",
    "The company's suppliers have been linked to unethical practices.",
    "Stakeholders express dissatisfaction with the company's ESG metrics.",
    "The organization faces backlash for neglecting worker safety.",
    "The firm's policies fail to address critical ESG issues.",
    "The company's energy efficiency measures are insufficient.",
    "The organization has ignored community feedback on key projects.",
    "The firm's response to climate change is widely criticized.",
    "The company's ESG initiatives are seen as greenwashing.",
    "The firm's contributions to social programs are minimal.",
    "The organization has not committed to a net-zero target.",
    "The company's waste disposal practices are harmful to the environment.",
    "Critics argue the firm's sustainability report lacks substance.",
    "The firm's lack of innovation in ESG initiatives is disappointing."
]

neutral_examples = [
    "The report provides general information about ESG metrics.",
    "There is no significant change in the company's sustainability efforts.",
    "The firm's ESG initiatives are neither harmful nor beneficial.",
    "The company's actions have minimal impact on ESG ratings.",
    "Neutral opinions were shared regarding the firm's ESG policies.",
    "The firm's latest ESG report highlights general updates.",
    "The company's sustainability efforts remain consistent with previous years.",
    "No major changes were observed in the company's ESG practices.",
    "The organization published a routine ESG compliance report.",
    "The firm's carbon footprint remains stable over the past year.",
    "The company's approach to ESG issues is neither groundbreaking nor inadequate.",
    "The organization's policies on social issues are standard industry practice.",
    "The company announced a review of its existing ESG policies.",
    "Stakeholders provided mixed feedback on the firm's ESG initiatives.",
    "The company's energy consumption levels remain average.",
    "The organization's annual report included an ESG summary.",
    "The firm's diversity metrics remain unchanged.",
    "The company's renewable energy usage is moderate.",
    "The organization reported no significant ESG risks this quarter.",
    "The company's waste recycling programs have seen minimal updates.",
    "Stakeholders remain undecided on the firm's ESG impact.",
    "The firm's environmental impact is within acceptable limits.",
    "The organization continues to comply with basic ESG standards.",
    "No noteworthy developments in the company's ESG strategy.",
    "The firm's approach to ESG remains consistent.",
    "The organization hosted a neutral discussion on sustainability.",
    "The firm's annual ESG report contains no surprises.",
    "The company's investment in ESG programs is modest.",
    "The organization's ESG strategy aligns with industry norms.",
    "No significant feedback on the company's latest ESG efforts.",
    "The firm's ESG rating remains unchanged.",
    "The organization announced its ESG roadmap for the next year.",
    "The firm's waste management policies are neither innovative nor lacking.",
    "The company's compliance with environmental laws is satisfactory.",
    "Stakeholders described the firm's ESG initiatives as average."
]

positive_examples = [
    "The company has been praised for its ESG initiatives.",
    "Stakeholders are happy with the firm's sustainability practices.",
    "The firm achieved its carbon neutrality goal ahead of schedule.",
    "The company's commitment to renewable energy is commendable.",
    "Positive feedback was received for the company's ESG contributions.",
    "The organization's waste management programs are highly effective.",
    "The firm's biodiversity initiatives have been widely appreciated.",
    "The company has set ambitious goals for reducing emissions.",
    "Stakeholders commend the organization's transparency in ESG reporting.",
    "The firm's energy efficiency programs have significantly reduced costs.",
    "The company is a leader in adopting renewable energy solutions.",
    "The firm's community outreach programs are making a real difference.",
    "The organization's diversity and inclusion efforts are exemplary.",
    "The company's ESG report highlights impressive progress.",
    "Stakeholders view the organization's climate change response positively.",
    "The firm's social responsibility initiatives are widely recognized.",
    "The organization is setting benchmarks for ESG practices.",
    "The company's efforts to improve worker safety are commendable.",
    "The firm has introduced innovative sustainability measures.",
    "The organization has won awards for its ESG contributions.",
    "The company's supply chain management reflects strong ESG principles.",
    "The firm has significantly reduced its carbon footprint.",
    "The organization's green energy initiatives are highly impactful.",
    "Stakeholders applaud the company's waste reduction strategies.",
    "The firm's leadership is committed to ESG excellence.",
    "The organization's water conservation programs are effective.",
    "The company leads its industry in ESG performance metrics.",
    "The firm's environmental restoration projects are impressive.",
    "The organization's ethical sourcing policies are well-implemented.",
    "The company's partnership with environmental groups is effective.",
    "The organization's ESG policies are an industry benchmark.",
    "The firm's transition to net-zero emissions is ahead of schedule.",
    "The company's investments in ESG programs are substantial.",
    "The firm's proactive approach to ESG issues is admirable.",
    "The organization has enhanced its renewable energy usage."
]

synthetic_data = {
    "Cleaned_Title": negative_examples + neutral_examples + positive_examples,
    "sentiment": [-1] * len(negative_examples) + [0] * len(neutral_examples) + [1] * len(positive_examples)
}

synthetic_df = pd.DataFrame(synthetic_data)

file_path = r"C:\Users\arjun\OneDrive\Documents\ESG\final_test.xlsx"
synthetic_df.to_excel(file_path, index=False)

print(f"Synthetic test data with 105 examples saved to {file_path}")
