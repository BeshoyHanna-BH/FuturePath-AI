from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import ttk

APP_NAME = "FuturePath AI"
APP_TAGLINE = "Find the career path that matches your strengths."
WINDOW_PADDING = 14

ACADEMIC_BACKGROUND_OPTIONS = [
    "STEM",
    "Health & Life Sciences",
    "Business & Social Sciences",
    "Arts & Humanities",
    "General / Undecided",
]

NUMERIC_FEATURES = [
    "math",
    "logic",
    "creativity",
    "communication",
    "coding",
    "biology",
    "interest_tech",
    "interest_design",
    "interest_business",
    "interest_helping_people",
]

SLIDER_FIELDS = [
    ("math", "Math", 6),
    ("logic", "Logic", 6),
    ("creativity", "Creativity", 6),
    ("communication", "Communication", 6),
    ("coding", "Coding", 4),
    ("biology", "Biology", 4),
    ("interest_tech", "Interest in Tech", 6),
    ("interest_design", "Interest in Design", 5),
    ("interest_business", "Interest in Business", 5),
    ("interest_helping_people", "Interest in Helping People", 5),
]

FEATURE_LABELS = {
    "math": "Math",
    "logic": "Logic",
    "creativity": "Creativity",
    "communication": "Communication",
    "coding": "Coding",
    "biology": "Biology",
    "interest_tech": "Interest in Tech",
    "interest_design": "Interest in Design",
    "interest_business": "Interest in Business",
    "interest_helping_people": "Interest in Helping People",
}

CAREER_PROFILES = {
    "Software Engineering": {
        "summary": "A strong fit for students who enjoy problem-solving, coding, and building useful systems.",
        "targets": {
            "math": 8,
            "logic": 9,
            "creativity": 6,
            "communication": 6,
            "coding": 9,
            "biology": 2,
            "interest_tech": 10,
            "interest_design": 4,
            "interest_business": 4,
            "interest_helping_people": 5,
        },
        "key_features": ["logic", "coding", "interest_tech"],
        "preferred_backgrounds": {
            "STEM": 1.0,
            "Health & Life Sciences": 0.7,
            "Business & Social Sciences": 0.7,
            "Arts & Humanities": 0.5,
            "General / Undecided": 0.8,
        },
        "roadmap": [
            "Learn Python fundamentals and problem-solving basics.",
            "Study data structures, algorithms, and object-oriented programming.",
            "Build 2-3 small apps and publish them on GitHub.",
            "Practice Git and GitHub for collaboration.",
        ],
    },
    "Data Science": {
        "summary": "Great for students who like numbers, analytical thinking, and turning data into decisions.",
        "targets": {
            "math": 9,
            "logic": 8,
            "creativity": 5,
            "communication": 5,
            "coding": 8,
            "biology": 4,
            "interest_tech": 9,
            "interest_design": 3,
            "interest_business": 6,
            "interest_helping_people": 4,
        },
        "key_features": ["math", "logic", "coding"],
        "preferred_backgrounds": {
            "STEM": 1.0,
            "Health & Life Sciences": 0.8,
            "Business & Social Sciences": 0.8,
            "Arts & Humanities": 0.5,
            "General / Undecided": 0.7,
        },
        "roadmap": [
            "Master Python and basic statistics.",
            "Learn data analysis with spreadsheets and simple visualization tools.",
            "Study machine learning fundamentals.",
            "Build a small real-world data project.",
        ],
    },
    "UI/UX Design": {
        "summary": "A strong option for students who combine creativity with empathy and user-centered thinking.",
        "targets": {
            "math": 4,
            "logic": 6,
            "creativity": 10,
            "communication": 8,
            "coding": 3,
            "biology": 1,
            "interest_tech": 7,
            "interest_design": 10,
            "interest_business": 5,
            "interest_helping_people": 6,
        },
        "key_features": ["creativity", "communication", "interest_design"],
        "preferred_backgrounds": {
            "STEM": 0.8,
            "Health & Life Sciences": 0.6,
            "Business & Social Sciences": 0.8,
            "Arts & Humanities": 1.0,
            "General / Undecided": 0.8,
        },
        "roadmap": [
            "Learn design basics, layout, and typography.",
            "Practice wireframing and prototyping with Figma.",
            "Study user research and usability testing.",
            "Create a portfolio with 2-3 case studies.",
        ],
    },
    "Digital Marketing": {
        "summary": "A practical fit for students who enjoy communication, campaigns, storytelling, and audience growth.",
        "targets": {
            "math": 4,
            "logic": 5,
            "creativity": 8,
            "communication": 10,
            "coding": 2,
            "biology": 1,
            "interest_tech": 5,
            "interest_design": 7,
            "interest_business": 10,
            "interest_helping_people": 7,
        },
        "key_features": ["communication", "interest_business", "creativity"],
        "preferred_backgrounds": {
            "STEM": 0.7,
            "Health & Life Sciences": 0.6,
            "Business & Social Sciences": 1.0,
            "Arts & Humanities": 0.9,
            "General / Undecided": 0.8,
        },
        "roadmap": [
            "Learn branding, content strategy, and customer journey basics.",
            "Study SEO, social media, and copywriting.",
            "Practice campaign planning and analytics.",
            "Run a small mock campaign and measure the results.",
        ],
    },
    "Biotechnology": {
        "summary": "Well suited to students who enjoy biology, experimentation, and applying science to real-world health problems.",
        "targets": {
            "math": 7,
            "logic": 7,
            "creativity": 5,
            "communication": 6,
            "coding": 3,
            "biology": 10,
            "interest_tech": 6,
            "interest_design": 2,
            "interest_business": 3,
            "interest_helping_people": 8,
        },
        "key_features": ["biology", "logic", "interest_helping_people"],
        "preferred_backgrounds": {
            "STEM": 0.8,
            "Health & Life Sciences": 1.0,
            "Business & Social Sciences": 0.5,
            "Arts & Humanities": 0.4,
            "General / Undecided": 0.7,
        },
        "roadmap": [
            "Strengthen biology and chemistry fundamentals.",
            "Explore genetics and biotechnology applications.",
            "Learn how technology supports healthcare innovation.",
            "Join a science activity or mini research project.",
        ],
    },
    "Business Analytics": {
        "summary": "A solid path for students who enjoy mixing business thinking with numbers and decision-making.",
        "targets": {
            "math": 7,
            "logic": 8,
            "creativity": 5,
            "communication": 8,
            "coding": 5,
            "biology": 2,
            "interest_tech": 7,
            "interest_design": 3,
            "interest_business": 9,
            "interest_helping_people": 6,
        },
        "key_features": ["logic", "communication", "interest_business"],
        "preferred_backgrounds": {
            "STEM": 0.9,
            "Health & Life Sciences": 0.7,
            "Business & Social Sciences": 1.0,
            "Arts & Humanities": 0.8,
            "General / Undecided": 0.8,
        },
        "roadmap": [
            "Learn Excel and business fundamentals.",
            "Study statistics and dashboard building.",
            "Practice SQL and data storytelling.",
            "Analyze a business case and present your findings.",
        ],
    },
}


def get_feature_label(feature_name: str) -> str:
    return FEATURE_LABELS.get(feature_name, feature_name.replace("_", " ").title())


def format_feature_list(features: list[str]) -> list[str]:
    return [get_feature_label(feature) for feature in features]


def join_readable(items: list[str]) -> str:
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return ", ".join(items[:-1]) + f", and {items[-1]}"


def pick_strengths(profile: dict[str, int | str], targets: dict[str, int], limit: int = 3) -> list[str]:
    ranked: list[tuple[float, float, str]] = []
    for feature_name, target_value in targets.items():
        user_value = float(profile[feature_name])
        closeness = 1 - (abs(user_value - target_value) / 10)
        if user_value >= target_value - 1:
            ranked.append((closeness, user_value, feature_name))
    ranked.sort(reverse=True)
    return [feature_name for _, _, feature_name in ranked[:limit]]


def pick_growth_areas(profile: dict[str, int | str], targets: dict[str, int], limit: int = 3) -> list[str]:
    ranked: list[tuple[float, str]] = []
    for feature_name, target_value in targets.items():
        user_value = float(profile[feature_name])
        gap = target_value - user_value
        if gap > 1:
            ranked.append((gap, feature_name))
    ranked.sort(reverse=True)
    return [feature_name for _, feature_name in ranked[:limit]]


def build_recommendation_reason(
    career: str,
    profile: dict[str, int | str],
    strengths: list[str],
    growth_areas: list[str],
) -> str:
    career_profile = CAREER_PROFILES[career]
    strengths_text = join_readable(format_feature_list(strengths))
    growth_text = join_readable(format_feature_list(growth_areas))

    parts = [career_profile["summary"]]
    if strengths_text:
        parts.append(f"Your strongest matching areas are {strengths_text}.")

    background_match_score = career_profile["preferred_backgrounds"].get(
        str(profile["academic_background"]), 0.5
    )
    if background_match_score >= 0.85:
        parts.append(
            f"Your {profile['academic_background']} background also supports this direction well."
        )

    if growth_text:
        parts.append(f"To become even stronger, focus next on {growth_text}.")

    return " ".join(parts)


def recommend_careers(user_profile: dict[str, int | str], top_k: int = 3) -> list[dict[str, object]]:
    scored_recommendations: list[dict[str, object]] = []

    for career_name, career_profile in CAREER_PROFILES.items():
        targets = career_profile["targets"]
        key_features = set(career_profile["key_features"])
        weighted_score = 0.0
        total_weight = 0.0

        for feature_name, target_value in targets.items():
            user_value = float(user_profile[feature_name])
            closeness = max(0.0, 1 - (abs(user_value - target_value) / 10))
            weight = 1.35 if feature_name in key_features else 1.0
            weighted_score += closeness * weight
            total_weight += weight

        feature_score = weighted_score / total_weight
        background_score = career_profile["preferred_backgrounds"].get(
            str(user_profile["academic_background"]), 0.45
        )
        final_score = ((feature_score * 0.86) + (background_score * 0.14)) * 100
        strengths = pick_strengths(user_profile, targets)
        growth_areas = pick_growth_areas(user_profile, targets)

        scored_recommendations.append(
            {
                "career": career_name,
                "score": round(final_score, 1),
                "confidence": round(final_score, 1),
                "strengths": format_feature_list(strengths),
                "growth_areas": format_feature_list(growth_areas),
                "reason": build_recommendation_reason(
                    career_name,
                    user_profile,
                    strengths,
                    growth_areas,
                ),
                "roadmap": career_profile["roadmap"],
            }
        )

    scored_recommendations.sort(key=lambda item: float(item["score"]), reverse=True)
    return scored_recommendations[:top_k]


class FuturePathApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title(APP_NAME)
        self.root.geometry("1120x840")
        self.root.minsize(980, 760)

        self.background_var = tk.StringVar(value=ACADEMIC_BACKGROUND_OPTIONS[0])
        self.slider_vars: dict[str, tk.IntVar] = {}
        self.scales: dict[str, ttk.Scale] = {}
        self.canvas: tk.Canvas | None = None
        self.scrollbar: ttk.Scrollbar | None = None
        self.main_frame: ttk.Frame | None = None
        self.canvas_window: int | None = None

        self._create_scroll_container()
        self._configure_style()
        self._build_layout()

    def _create_scroll_container(self) -> None:
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(
            self.root,
            highlightthickness=0,
            borderwidth=0,
            background="#f4f6f8",
        )
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.main_frame = ttk.Frame(self.canvas, padding=WINDOW_PADDING)
        self.canvas_window = self.canvas.create_window((0, 0), window=self.main_frame, anchor="nw")

        self.main_frame.bind("<Configure>", self._sync_scroll_region)
        self.canvas.bind("<Configure>", self._sync_canvas_width)
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)

    def _sync_scroll_region(self, _event: tk.Event) -> None:
        if self.canvas is not None:
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def _sync_canvas_width(self, event: tk.Event) -> None:
        if self.canvas is not None and self.canvas_window is not None:
            self.canvas.itemconfigure(self.canvas_window, width=event.width)

    def _on_mouse_wheel(self, event: tk.Event) -> None:
        if self.canvas is not None:
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def _scroll_to_results(self) -> None:
        if self.canvas is not None:
            self.canvas.yview_moveto(1.0)

    def _scroll_to_top(self) -> None:
        if self.canvas is not None:
            self.canvas.yview_moveto(0.0)

    def _configure_style(self) -> None:
        style = ttk.Style(self.root)
        try:
            if "vista" in style.theme_names():
                style.theme_use("vista")
        except tk.TclError:
            pass

        style.configure("Hero.TFrame", background="#0f355d")
        style.configure("HeroTitle.TLabel", background="#0f355d", foreground="#f4fbfb")
        style.configure("HeroTagline.TLabel", background="#0f355d", foreground="#cfe9e6")
        style.configure("HeroHint.TLabel", background="#0f355d", foreground="#f9d977")
        style.configure("Primary.TButton", padding=(14, 8))

    def _build_layout(self) -> None:
        parent = self.main_frame
        if parent is None:
            raise RuntimeError("Main frame was not initialized.")

        hero_frame = ttk.Frame(parent, style="Hero.TFrame", padding=22)
        hero_frame.grid(row=0, column=0, sticky="ew", pady=(0, 12))

        ttk.Label(
            hero_frame,
            text=APP_NAME,
            style="HeroTitle.TLabel",
            font=("Segoe UI", 28, "bold"),
        ).grid(row=0, column=0, sticky="w")

        ttk.Label(
            hero_frame,
            text=APP_TAGLINE,
            style="HeroTagline.TLabel",
            font=("Segoe UI", 12, "bold"),
        ).grid(row=1, column=0, sticky="w", pady=(6, 2))

        ttk.Label(
            hero_frame,
            text="Single-file Python version. Double-click to run with Python installed.",
            style="HeroTagline.TLabel",
            font=("Segoe UI", 10),
        ).grid(row=2, column=0, sticky="w")

        ttk.Label(
            hero_frame,
            text="Use the scrollbar on the right or the buttons below to jump up and down.",
            style="HeroHint.TLabel",
            font=("Segoe UI", 10),
        ).grid(row=3, column=0, sticky="w", pady=(8, 0))

        profile_frame = ttk.LabelFrame(parent, text="Your profile", padding=12)
        profile_frame.grid(row=1, column=0, sticky="nsew")

        ttk.Label(profile_frame, text="Academic background").grid(
            row=0, column=0, sticky="w", pady=(0, 8)
        )
        ttk.Combobox(
            profile_frame,
            textvariable=self.background_var,
            values=ACADEMIC_BACKGROUND_OPTIONS,
            state="readonly",
            width=28,
        ).grid(row=0, column=1, sticky="w", pady=(0, 8))

        ttk.Label(profile_frame, text="Rate yourself from 0 to 10").grid(
            row=1, column=0, columnspan=2, sticky="w", pady=(0, 10)
        )

        for index, (field_name, label_text, default_value) in enumerate(SLIDER_FIELDS, start=2):
            value_var = tk.IntVar(value=default_value)
            self.slider_vars[field_name] = value_var

            ttk.Label(profile_frame, text=label_text).grid(row=index, column=0, sticky="w")
            scale = ttk.Scale(
                profile_frame,
                from_=0,
                to=10,
                orient="horizontal",
                variable=value_var,
                command=lambda value, name=field_name: self.slider_vars[name].set(
                    int(round(float(value)))
                ),
            )
            scale.set(default_value)
            scale.grid(row=index, column=1, sticky="ew", padx=(8, 10))
            self.scales[field_name] = scale

            ttk.Label(profile_frame, textvariable=value_var, width=3).grid(
                row=index, column=2, sticky="w"
            )

        profile_frame.columnconfigure(1, weight=1)

        buttons_frame = ttk.Frame(parent)
        buttons_frame.grid(row=2, column=0, sticky="ew", pady=(12, 12))

        ttk.Button(
            buttons_frame,
            text="Analyze My Fit",
            command=self.generate_recommendations,
            style="Primary.TButton",
        ).grid(row=0, column=0, sticky="w")

        ttk.Button(
            buttons_frame,
            text="Reset Scores",
            command=self.reset_scores,
        ).grid(row=0, column=1, sticky="w", padx=(8, 0))

        ttk.Button(
            buttons_frame,
            text="Scroll To Results",
            command=self._scroll_to_results,
        ).grid(row=0, column=2, sticky="w", padx=(8, 0))

        ttk.Button(
            buttons_frame,
            text="Back To Top",
            command=self._scroll_to_top,
        ).grid(row=0, column=3, sticky="w", padx=(8, 0))

        results_frame = ttk.LabelFrame(parent, text="Career recommendations", padding=12)
        results_frame.grid(row=3, column=0, sticky="nsew")

        self.results_box = scrolledtext.ScrolledText(
            results_frame,
            wrap=tk.WORD,
            font=("Segoe UI", 10),
            height=26,
        )
        self.results_box.grid(row=0, column=0, sticky="nsew")
        self.results_box.insert(
            tk.END,
            "Welcome to FuturePath AI.\n\nChoose your academic background, rate your skills honestly, then click 'Analyze My Fit' to get your top career matches with reasons and a roadmap.",
        )
        self.results_box.configure(state="disabled")

        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)

    def collect_profile(self) -> dict[str, int | str]:
        profile = {"academic_background": self.background_var.get()}
        for field_name, value_var in self.slider_vars.items():
            profile[field_name] = value_var.get()
        return profile

    def reset_scores(self) -> None:
        for field_name, _, default_value in SLIDER_FIELDS:
            self.slider_vars[field_name].set(default_value)
            self.scales[field_name].set(default_value)
        self._scroll_to_top()

    def render_results(self, recommendations: list[dict[str, object]]) -> None:
        lines: list[str] = []
        top_choice = recommendations[0]
        lines.append(f"Top recommendation: {top_choice['career']} ({top_choice['score']}% fit score)")
        lines.append("")
        lines.append(str(top_choice["reason"]))
        lines.append("")

        for index, recommendation in enumerate(recommendations, start=1):
            lines.append(f"{index}. {recommendation['career']}")
            lines.append(f"Match score: {recommendation['score']}%")
            lines.append(f"Confidence: {recommendation['confidence']}%")
            lines.append(str(recommendation["reason"]))
            lines.append("Strengths:")
            for item in recommendation["strengths"]:
                lines.append(f"  - {item}")
            lines.append("Improve next:")
            growth_areas = recommendation["growth_areas"] or [
                "You already have a strong starting profile for this path."
            ]
            for item in growth_areas:
                lines.append(f"  - {item}")
            lines.append("Starter roadmap:")
            for step in recommendation["roadmap"]:
                lines.append(f"  - {step}")
            lines.append("")

        self.results_box.configure(state="normal")
        self.results_box.delete("1.0", tk.END)
        self.results_box.insert(tk.END, "\n".join(lines).strip())
        self.results_box.configure(state="disabled")

    def generate_recommendations(self) -> None:
        try:
            profile = self.collect_profile()
            recommendations = recommend_careers(profile, top_k=3)
            self.render_results(recommendations)
            self._scroll_to_results()
        except Exception as exc:
            messagebox.showerror(APP_NAME, f"Something went wrong:\n{exc}")


def main() -> None:
    root = tk.Tk()
    FuturePathApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
