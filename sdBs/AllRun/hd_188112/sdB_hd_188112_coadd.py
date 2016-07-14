from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[298.630792,-28.339139],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_hd_188112/sdB_hd_188112_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_hd_188112/sdB_hd_188112_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
