package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"path"
	"time"

	"github.com/gorilla/mux"
)

var dwarf_api = "https://thedwarves.pusherplatform.io/api/dwarves"

type Dwarf struct {
	Dwarf DwarfInfo
}

type DwarfInfo struct {
	Name    string `json:"name"`
	Birth   string `json:"birth"`
	Death   string `json:"death"`
	Culture string `json:"culture"`
}

type Dwarves struct {
	Dwarves []DwarfInfo `json:"dwarves"`
}

func scrape_json(url string, target interface{}) error {
	resp, _ := http.Get(url)
	bytes, _ := ioutil.ReadAll(resp.Body)
	defer resp.Body.Close()
	return json.Unmarshal(bytes, &target)
}

func lookup_handler(w http.ResponseWriter, r *http.Request) {
	queriedName := path.Base(r.URL.Path)

	var dwarves Dwarves
	err := scrape_json(dwarf_api, &dwarves)
	if err != nil {
		fmt.Println(err)
	}

	for _, v := range dwarves.Dwarves {
		if v.Name == queriedName {
			dwarf := Dwarf{v}
			n, _ := json.Marshal(dwarf)
			w.Header().Set("Content-Type", "application/json")
			w.Write(n)
			break
		}
	}
}

func names_handler(w http.ResponseWriter, r *http.Request) {
	var dwarves Dwarves
	err := scrape_json(dwarf_api, &dwarves)
	if err != nil {
		fmt.Println(err)
	}

	names := make(map[string][]string)
	for _, v := range dwarves.Dwarves {
		names["dwarves"] = append(names["dwarves"], v.Name)
	}

	n, _ := json.Marshal(names)
	w.Header().Set("Content-Type", "application/json")
	w.Write(n)
}

func main() {
	r := mux.NewRouter()
	r.HandleFunc("/api/dwarves", names_handler)
	r.HandleFunc("/api/dwarves/{name}", lookup_handler)

	srv := &http.Server{
		Handler: r,
		Addr:    "0.0.0.0:8000",
		// Good practice: enforce timeouts for servers you create!
		WriteTimeout: 15 * time.Second,
		ReadTimeout:  15 * time.Second,
	}

	srv.ListenAndServe()
}
