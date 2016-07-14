from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[356.253333,42.949056],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_234500.80+425656.6/sdB_sdssj_234500.80+425656.6_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_234500.80+425656.6/sdB_sdssj_234500.80+425656.6_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
