from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[27.17075,36.564083],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_FBS_0145+363/sdB_FBS_0145+363_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_FBS_0145+363/sdB_FBS_0145+363_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
