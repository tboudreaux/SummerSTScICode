from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[166.076,4.537889],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_110418.24+043216.4/sdB_sdssj_110418.24+043216.4_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_110418.24+043216.4/sdB_sdssj_110418.24+043216.4_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
