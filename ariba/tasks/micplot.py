import argparse
import ariba

def run(options):
    plotter = ariba.mic_plotter.MicPlotter(
      options.prepareref_dir,
      options.antibiotic,
      options.mic_file,
      options.summary_file,
      options.outprefix,
      use_hets=options.use_hets,
      main_title=options.main_title,
      plot_height=options.plot_height,
      plot_width=options.plot_width,
      log_y=options.log_y,
      plot_types=options.plot_types,
      jitter_width=options.jitter_width,
      no_combinations=options.no_combinations,
      hlines=options.hlines,
      point_size=options.point_size,
      point_range=options.point_range,
      point_break=options.point_break,
      dot_size=options.dot_size,
      dot_outline=options.dot_outline,
      dot_y_text_size=options.dot_y_text_size,
      panel_heights=options.panel_heights,
      colourmap=options.colourmap,
      number_of_colours=options.number_of_colours,
      colour_skip=options.colour_skip,
      interrupted=options.interrupted,
      violin_width=options.violin_width,
      xkcd=options.xkcd,
      min_samples=options.min_samples
    )

    plotter.run()
