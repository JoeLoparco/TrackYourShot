# TrackYourShot 🏀

A Strava-inspired web application for basketball players to track their training, monitor progress, and elevate their game through comprehensive analytics and community features.

## 📋 Overview

TrackYourShot is designed to help basketball players at every level track their performance, analyze their shooting patterns, monitor workout intensity, and connect with other players. Whether you're a high school athlete, college player, or weekend warrior, TrackYourShot provides the tools you need to improve your game.

## ✨ Features

### Current Features
- **User Authentication** - Secure login and registration system
- **User Dashboard** - Personalized hub for tracking progress
- **Responsive Design** - Mobile-friendly interface built with Bootstrap

### Planned Features
- **🏃‍♂️ Workout Intensity Tracking**
  - Heart rate monitoring integration
  - RPE (Rate of Perceived Exertion) scale tracking
  - Workout duration and fatigue level analysis

- **🎯 Advanced Shot Analytics**
  - Interactive shot charts with heat maps
  - Accuracy tracking by court zone
  - Shot type breakdown and trends
  - Performance analysis over time

- **📊 Skill Development**
  - Skill level assessment tools
  - Peer comparison and benchmarking
  - Progress visualization and goal setting

- **🏆 Drill Performance**
  - Custom drill creation and tracking
  - Performance metrics and improvement trends
  - Training routine optimization

- **👥 Community & Social Features**
  - Follow other players
  - Team challenges and competitions
  - Achievement badges and milestones

- **🎮 Game Performance**
  - Game statistics tracking
  - Performance correlation with training
  - Season-long analytics

## 🛠️ Tech Stack

- **Backend**: Python Flask
- **Database**: PostgreSQL (hosted on Render)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Template Engine**: Jinja2
- **ORM**: SQLAlchemy
- **Authentication**: Flask sessions
- **Environment Management**: python-dotenv

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- Virtual environment support

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/TrackYourShot.git
   cd TrackYourShot
   ```

2. **Set up virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the project root:
   ```env
   DATABASE_URL=your_postgresql_connection_string
   SECRET_KEY=your_secret_key_here
   FLASK_ENV=development
   FLASK_DEBUG=True
   ```

5. **Initialize the database**
   ```bash
   python create_tables.py
   ```

6. **Run the application**
   ```bash
   python -m flask run
   # or
   python app.py
   ```

7. **Open your browser**
   
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
TrackYourShot/
├── app/
│   ├── __init__.py          # Flask app initialization and configuration
│   ├── routes/
│   │   ├── auth.py          # Authentication routes
│   │   └── routes.py        # Main application routes
│   ├── static/
│   │   ├── styles.css       # Custom CSS styles
│   │   └── js/              # JavaScript files
│   └── templates/
│       ├── base.html        # Base template
│       ├── index.html       # Landing page
│       ├── login.html       # Login page
│       └── ...              # Other templates
├── create_tables.py         # Database initialization script
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (not in git)
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## 🗄️ Database Schema

### User Model
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
```

*Additional models for workouts, shots, drills, and social features coming soon...*

## 🎨 Design Philosophy

TrackYourShot is built with a mobile-first approach, ensuring basketball players can log their training and view their progress on any device. The interface prioritizes:

- **Simplicity**: Quick data entry during or after workouts
- **Visual Analytics**: Clear charts and graphs for performance insights
- **Community**: Social features to motivate and connect players
- **Accessibility**: Usable by players of all technical skill levels

## 🚧 Development Status

This project is currently in active development. We're building the MVP with core tracking features first, then expanding into advanced analytics and social features.

**Current Phase**: Foundation & Authentication
**Next Phase**: Core tracking features and database models

## 🤝 Contributing

This is a learning project, but contributions and feedback are welcome! If you'd like to contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🎯 Roadmap

- [ ] Complete user authentication system
- [ ] Build workout logging interface
- [ ] Implement basic shot tracking
- [ ] Add progress visualization
- [ ] Create user dashboard
- [ ] Develop mobile-responsive design
- [ ] Add social features
- [ ] Implement advanced analytics
- [ ] Deploy to production

## 📧 Contact

**Developer**: Joseph Loparco
**Email**: loparcoJoseph@gmail.com
**Project Link**: [https://github.com/yourusername/TrackYourShot](https://github.com/yourusername/TrackYourShot)

---

*Built with ❤️ for the basketball community*
