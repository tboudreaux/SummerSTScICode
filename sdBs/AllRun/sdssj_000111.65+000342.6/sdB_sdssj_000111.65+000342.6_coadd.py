from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[0.298542,0.061833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_000111.65+000342.6/sdB_sdssj_000111.65+000342.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_000111.65+000342.6/sdB_sdssj_000111.65+000342.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
