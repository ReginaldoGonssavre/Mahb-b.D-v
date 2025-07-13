
"use client"

import { useState, useEffect } from 'react';
import { motion } from "framer-motion"
import { TrendingUp, TrendingDown, Zap } from "lucide-react"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "../components/ui/card"
import { generatePortfolioData } from '../lib/quantum-simulator';

export default function QuantumPortfolio() {
  const [data, setData] = useState(null);

  useEffect(() => {
    setData(generatePortfolioData());
  }, []);

  if (!data) {
    return (
      <Card className="bg-slate-800/50 backdrop-blur-md border-slate-700/50">
        <CardHeader>
          <CardTitle className="text-white">Loading Portfolio...</CardTitle>
        </CardHeader>
      </Card>
    )
  }

  return (
    <div className="space-y-6 p-4 md:p-6">
      {/* Portfolio Overview */}
      <Card className="bg-slate-800/50 backdrop-blur-md border-slate-700/50">
        <CardHeader>
          <CardTitle className="text-white flex items-center gap-2">
            <Zap className="h-5 w-5 text-cyan-400 flex-shrink-0" />
            <span className="flex-1 min-w-0">Quantum Portfolio</span>
          </CardTitle>
          <CardDescription className="text-gray-400 text-balance">AI-powered quantum asset management</CardDescription>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
            <div className="text-center">
              <div className="text-sm text-gray-400">Entanglement Efficiency</div>
              <div className="text-lg font-bold text-cyan-400">
                {(data.quantum_metrics.entanglement_efficiency * 100).toFixed(1)}%
              </div>
            </div>
            <div className="text-center">
              <div className="text-sm text-gray-400">Superposition Advantage</div>
              <div className="text-lg font-bold text-purple-400">
                {(data.quantum_metrics.superposition_advantage * 100).toFixed(1)}%
              </div>
            </div>
            <div className="text-center">
              <div className="text-sm text-gray-400">Decoherence Resistance</div>
              <div className="text-lg font-bold text-green-400">
                {(data.quantum_metrics.decoherence_resistance * 100).toFixed(1)}%
              </div>
            </div>
            <div className="text-center">
              <div className="text-sm text-gray-400">Quantum Speedup</div>
              <div className="text-lg font-bold text-orange-400">
                {data.quantum_metrics.quantum_speedup.toFixed(2)}x
              </div>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Assets List */}
      <Card className="bg-slate-800/50 backdrop-blur-md border-slate-700/50">
        <CardHeader>
          <CardTitle className="text-white">Quantum Assets</CardTitle>
          <CardDescription className="text-gray-400 text-balance">
            Your quantum-enhanced digital asset portfolio
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {data.assets.map((asset, index) => (
              <motion.div
                key={asset.symbol}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
                className="flex items-center justify-between p-4 bg-slate-700/30 rounded-lg hover:bg-slate-700/50 transition-colors"
              >
                <div className="flex items-center gap-4">
                  <div className="w-10 h-10 bg-gradient-to-r from-cyan-400 to-purple-400 rounded-full flex items-center justify-center">
                    <span className="text-white font-bold text-sm">{asset.symbol.slice(0, 2)}</span>
                  </div>
                  <div>
                    <div className="font-semibold text-white">{asset.symbol}</div>
                    <div className="text-sm text-gray-400">{asset.name}</div>
                    <div className="text-xs text-cyan-400">
                      Quantum Correlation: {(asset.quantum_correlation * 100).toFixed(0)}%
                    </div>
                  </div>
                </div>

                <div className="text-right">
                  <div className="font-semibold text-white">${asset.value.toLocaleString()}</div>
                  <div className="text-sm text-gray-400">
                    {asset.quantity.toFixed(4)} @ ${asset.price.toLocaleString()}
                  </div>
                  <div
                    className={`text-sm flex items-center justify-end gap-1 ${asset.change_24h >= 0 ? "text-green-400" : "text-red-400"}`}
                  >
                    {asset.change_24h >= 0 ? <TrendingUp className="h-4 w-4" /> : <TrendingDown className="h-4 w-4" />}
                    <span>
                      {asset.change_24h >= 0 ? "+" : ""}
                      {asset.change_24h.toFixed(2)}%
                    </span>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        </CardContent>
      </Card>
    </div>
  )
}
