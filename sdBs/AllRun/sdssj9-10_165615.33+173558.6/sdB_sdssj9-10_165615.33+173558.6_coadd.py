from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[254.063875,17.599611],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj9-10_165615.33+173558.6/sdB_sdssj9-10_165615.33+173558.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj9-10_165615.33+173558.6/sdB_sdssj9-10_165615.33+173558.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
