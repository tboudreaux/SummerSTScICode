from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[183.487708,3.984194],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_121357.05+035903.1/sdB_sdssj9-10_121357.05+035903.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_121357.05+035903.1/sdB_sdssj9-10_121357.05+035903.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
