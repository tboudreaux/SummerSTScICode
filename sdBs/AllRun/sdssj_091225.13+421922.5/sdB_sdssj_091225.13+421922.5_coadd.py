from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[138.104708,42.322917],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_091225.13+421922.5/sdB_sdssj_091225.13+421922.5_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_091225.13+421922.5/sdB_sdssj_091225.13+421922.5_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
