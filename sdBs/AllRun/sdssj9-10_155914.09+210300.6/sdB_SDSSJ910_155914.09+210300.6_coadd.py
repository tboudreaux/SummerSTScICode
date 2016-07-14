from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[239.808708,21.050167],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_SDSSJ910_155914.09+210300.6/sdB_SDSSJ910_155914.09+210300.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_SDSSJ910_155914.09+210300.6/sdB_SDSSJ910_155914.09+210300.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
