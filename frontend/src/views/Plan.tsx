import { Container } from "@components";

export default function Plan(): React.ReactNode {
  return (
    <Container>
      <article className="mx-auto max-w-3xl space-y-10">
        <header className="space-y-2">
          <h1 className="font-heading text-heading-pink text-4xl font-black tracking-tight uppercase">
            The Game Plan
          </h1>
        </header>

        <section className="space-y-3">
          <h2 className="font-heading text-heading-blue text-xl font-bold">
            Why are we doing this?
          </h2>
          <p className="text-muted leading-relaxed">
            PUCKCURL! is a fan-organized initiative designed to turn a negative
            into a positive. Since Britta Curl-Salemme has joined the PWHL, fans
            have made their feelings about her publicly stated views clear. Our
            goal is to provide a positive outlet for fans who feel frustrated
            and hurt by Curl's views. It is our belief that choosing to step
            away from supporting a team she is on only serves to remove good
            people from those spaces. We hope that this donation tracker will
            help bring fans together with a goal of fighting back by putting our
            money where our mouth is!
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="font-heading text-heading-blue text-xl font-bold">
            Why does it matter?{" "}
          </h2>
          <p className="text-muted leading-relaxed">
            It is important to let the league know how we feel, by making our
            voices heard. However, given that the league has not historically
            made any changes as a result of the fans' protests, it's just as
            important to support the organizations and foundations that are
            working to make the world a better and more inclusive place. The
            charities we recommend have been researched by our team and are
            actively doing the work to facilitate change and create supportive
            environments for LGBTQ+ and BIPOC individuals, particularly in the
            Detroit area but also on a national scale. When you choose to donate
            in protest of Curl, you become an active playmaker as a part of that
            change!
          </p>
        </section>
      </article>
    </Container>
  );
}
