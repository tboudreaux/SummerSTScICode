from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[231.392292,9.980833],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_152534.15+095851.0/sdB_sdssj_152534.15+095851.0_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_152534.15+095851.0/sdB_sdssj_152534.15+095851.0_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()