from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[23.71325,-9.168417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_013451.18-091006.3/sdB_sdssj_013451.18-091006.3_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_013451.18-091006.3/sdB_sdssj_013451.18-091006.3_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
