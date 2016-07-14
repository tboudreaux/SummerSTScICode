from gPhoton.gMap import gMap
def main():
	gMap(band="NUV", skypos=[199.89425,9.496417],  skyrange=[0.0333333333333,0.0333333333333], stepsz = 30., cntfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdBs/sdB_sdssj_131934.62+092947.1/sdB_sdssj_131934.62+092947.1_movie_count.fits", cntcoaddfile="/data2/fleming/GPHOTON_OUTPUT/LIGHTCURVES/sdB/sdB_sdssj_131934.62+092947.1/sdB_sdssj_131934.62+092947.1_count_coadd.fits", overwrite=True, verbose=3)
if __name__ == "__main__":
	main()
