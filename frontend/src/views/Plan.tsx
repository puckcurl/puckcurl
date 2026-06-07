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
            help bring fans together with a common goal of good.
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="font-heading text-heading-blue text-xl font-bold">
            Why does it matter?
          </h2>
          <p className="text-muted leading-relaxed">
            It is important to let the league know how we feel by making our
            voices heard. However, it's just as important to support the
            organizations and foundations that are working to make the world a
            better and more inclusive place. The charities we recommend are
            actively doing the work to facilitate change and create supportive
            environments for LGBTQ+ and BIPOC individuals, particularly in the
            Detroit area but also on a national scale. When you choose to donate
            in protest, you become an active playmaker as a part of that change!
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="font-heading text-heading-blue text-xl font-bold">
            How does it work?
          </h2>
          <p className="text-muted leading-relaxed">
            The idea is that for every goal Curl scores, fans mobilize to donate
            to a charity of their choice and we record the progress here. We
            don't want anyone to feel constrained by these parameters. You are
            welcome to donate for any reason at all, and in any amount that
            feels right for you. You can donate for every penalty she serves, or
            for every point she gets, or every game she plays in. You can donate
            repeatedly or just once. We will happily catalogue every donation
            made in protest of her views.
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="font-heading text-heading-blue text-xl font-bold">
            Who are we?
          </h2>
          <p className="text-muted leading-relaxed">
            We are a group of PWHL fans who have decided to channel our anger
            and frustration into positive change. Both trans and cis fans have
            come together to create this initiative and get it off the ground,
            from building the website to collecting a list of charities to
            setting up social media accounts to moderating incoming donations.
            Fans across the queer spectrum and allies alike are coming together
            in the face of transphobia to make a statement: hockey is for
            everyone.
          </p>
        </section>

        <section className="space-y-3">
          <h2 className="font-heading text-heading-blue text-xl font-bold">
            Is this the best approach?
          </h2>
          <p className="text-muted leading-relaxed">
            We don't know, but to this group of fans, it feels better than
            resignation. Since Britta Curl-Salemme was drafted to the PWHL, fans
            have been vocal about their outrage. Emails and letters have been
            sent, phone calls have been made, tickets have been cancelled, and
            games have been boycotted. Fans have booed whenever Curl touches the
            puck; booed even more when she scores. It is likely that many other
            players in the league share Curl's views and have simply kept quiet
            about it. Curl's move to Detroit reminded everyone that any team in
            the league would sign her given the chance-- she plays good hockey.
            For us, it provided the push needed to find another way of making
            our voices heard. Regardless of the impact on the league, at least
            this method of protest puts money into the organizations that fight
            for inclusion on a daily basis, and we think that matters.
          </p>
        </section>
      </article>
    </Container>
  );
}
