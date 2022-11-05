mport Link from 'next/link';  // doesn't seem to be loaded! (removed the i)

xport default function CustomLink({ children, href }) {
    if href.startsWith('http') {
      if href.includes('wikipedia') {
          console.log("wp");
        return <a
              href={href}
              target="_blank"
              rel="noopener noreferrer"
              className={"link-wp"}
          >{"WP"}
              {children}
          </a>
      }
          console.log("ext");
      return <a
              href={href}
              target="_blank"
              rel="noopener noreferrer"
              className={"link-ext"}
          >"ext"
              {children}
          </a>
    }
          console.log("int");
    return <Link href={href} className={"tuancao"}>
            <a>"int"
                {children}
            </a>
        </Link>
    }
}
