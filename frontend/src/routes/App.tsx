import { Navigate, Route, Routes } from 'react-router-dom'
import LandingPage from '../pages/LandingPage'
import LiveScoresPage from '../pages/LiveScoresPage'
import TeamsPage from '../pages/TeamsPage'
import HostelBlocksPage from '../pages/HostelBlocksPage'
import AboutPage from '../pages/AboutPage'
import GuidelinesPage from '../pages/GuidelinesPage'
import AdminLoginPage from '../pages/admin/AdminLoginPage'
import AdminDashboardPage from '../pages/admin/AdminDashboardPage'

export default function App() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/live-scores" element={<LiveScoresPage />} />
      <Route path="/teams" element={<TeamsPage />} />
      <Route path="/hostel-blocks" element={<HostelBlocksPage />} />
      <Route path="/about" element={<AboutPage />} />
      <Route path="/guidelines" element={<GuidelinesPage />} />

      <Route path="/admin/login" element={<AdminLoginPage />} />
      <Route path="/admin" element={<AdminDashboardPage />} />

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  )
}
