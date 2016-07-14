from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[315.869833,0.250833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_210328.76-001503.0/sdB_sdssj_210328.76-001503.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_210328.76-001503.0/sdB_sdssj_210328.76-001503.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
