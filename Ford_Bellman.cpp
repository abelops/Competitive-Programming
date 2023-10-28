#include <iostream>
#include <vector>
#include <climits>

using namespace std;

void solve() {
    int n, m;
    cin >> n >> m;
    
    vector<long long> dist(n, LLONG_MAX);
    dist[0] = 0;
    
    vector<vector<int>> graph;
    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        graph.push_back({u, v, w});
    }
    
    for (int i = 0; i < n - 1; i++) {
        for (const auto& edge : graph) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            
            if (dist[u-1] != LLONG_MAX && dist[u-1] + w < dist[v-1]) {
                dist[v-1] = dist[u-1] + w;
            }
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (dist[i] == LLONG_MAX) {
            dist[i] = 30000;
        }
    }
    
    for (int i = 0; i < n; i++) {
        cout << dist[i] << " ";
    }
    cout << endl;
}

int main() {
    solve();
    return 0;
}