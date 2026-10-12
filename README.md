# Awesome Rustified

Liste publique d’applications **open source** recodées en **Rust**, souvent pour remplacer des clients **Electron**, **navigateur embarqué**, ou des applis **propriétaires** lourdes — avec le même job, moins de complexité sous le capot.

> Projets listés à titre informatif. Marques citées = propriétaires respectifs. Pas d’affiliation.

## Sommaire

- [Comment lire cette liste](#comment-lire-cette-liste)
- [Modèle d’entrée](#modèle-dentrée)
- [Musique & streaming](#musique--streaming)
- [Messagerie](#messagerie)
- [À classer](#à-classer)
- [Contribuer](#contribuer)

## Comment lire cette liste

| Champ | Signification |
|--------|----------------|
| **Remplace / alternative à** | Produit ou type d’app d’origine (souvent fermé ou très lourd) |
| **Stack** | Bibliothèques / UI Rust notables |
| **Pourquoi Rust** | Ce qu’on gagne en pratique (RAM, démarrage, pas de Chromium, binaire unique, etc.) |

Les entrées sont triées **par catégorie**, pas par « qualité » ou popularité.

## Modèle d’entrée

Quand tu ajoutes une app, copie ce bloc dans la bonne section :

```markdown
### NomDuProjet

- **Remplace / alternative à :** …
- **Repo :** https://github.com/…
- **Site :** https://… (optionnel)
- **Licence :** …
- **Plateformes :** Linux, macOS, Windows, …
- **Stack :** …
- **Pourquoi Rust :** une ou deux phrases, factuelles.
- **Notes :** prérequis, limites connues, renommage récent, etc. (optionnel)
```

---

## Musique & streaming

### Spotifast

- **Remplace / alternative à :** client desktop **Spotify** (souvent Electron / empreinte mémoire élevée)
- **Repo :** [crmne/spotifast](https://github.com/crmne/spotifast)
- **Site :** [spotifast.rocks](https://spotifast.rocks/)
- **Licence :** MIT
- **Plateformes :** Linux, macOS, Windows
- **Stack :** [egui](https://github.com/emilk/egui), [librespot](https://github.com/librespot-org/librespot), [fastframe](https://github.com/crmne/fastframe) (fondation partagée avec ZapFast)
- **Pourquoi Rust :** client natif, **sans moteur de navigateur** ; démarrage rapide ; usage mémoire typique annoncé autour de **100–250 Mo** (vs souvent **600 Mo–1 Go+** côté app officielle).
- **Notes :** ex-**Fastpotify** (renommage vers 0.8.0). Lecture via librespot + API Spotify ; Spotify Connect, bibliothèque, contrôles MPRIS sur Linux. Projet indépendant, non affilié à Spotify AB.

---

## Messagerie

### ZapFast

- **Remplace / alternative à :** **WhatsApp Web** / clients desktop type Electron ; pas d’app Linux officielle WhatsApp
- **Repo :** [crmne/zapfast](https://github.com/crmne/zapfast)
- **Site :** [zapfast.rocks](https://zapfast.rocks/)
- **Licence :** MIT
- **Plateformes :** Linux, macOS, Windows
- **Stack :** egui, [whatsapp-rust](https://github.com/crmne/whatsapp-rust) (lignée whatsmeow), fastframe
- **Pourquoi Rust :** binaire unique, **pas de Chromium** ; ouverture rapide ; ~**200 Mo** RAM à l’idle en test publié (vs ~**1,13 Go** pour WhatsApp Web + Chromium sur leur bench Linux).
- **Notes :** appareil **companion** lié au téléphone (modèle WhatsApp Web). Frère de Spotifast sur la même base fastframe. Projet indépendant, non affilié à WhatsApp / Meta.

---

## À classer

Bac à sable pour la suite — déplace chaque entrée dans une section quand tu es sûr de la catégorie.

| Projet | Remplace (idée) | Repo | Statut liste |
|--------|------------------|------|----------------|
| *…* | *…* | *…* | brouillon / validé |

**Catégories prévues** (on ajoute seulement quand il y a au moins une entrée) :

- Productivité & bureautique
- Développement & DevOps
- Réseaux sociaux & forums
- Lecture & médias (hors musique)
- Système & utilitaires desktop
- Jeux & émulation (clients, pas moteurs de jeu)

---

## Contribuer

1. Vérifie que le projet est **open source** sur GitHub (ou forge équivalente) et **écrit principalement en Rust** pour le client desktop / l’app listée.
2. Ajoute une entrée au format ci-dessus ; une phrase « pourquoi Rust » suffit — pas besoin de marketing.
3. Si le projet remplace un truc payant ou fermé, dis **quoi** (ex. « client X », pas juste « alternative »).
4. Ouvre une PR ou un issue avec le lien repo + catégorie proposée.

**On évite :** forks morts sans maintenance, démos sans usage réel, ou réimplémentations qui ne font que wrapper le produit officiel dans un autre shell.

---

## Licence de cette liste

Le **contenu** de ce dépôt (texte, structure) : [CC0 1.0](LICENSE) — fais-en ce que tu veux. Chaque projet listé garde **sa** licence.
