from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[347.546292,-32.701069],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_gd_1532/sdB_gd_1532_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_gd_1532/sdB_gd_1532_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
